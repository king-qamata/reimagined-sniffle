import re
import logging

from email.charset import Charset as EMailCharset
from email.utils import parsedate_to_datetime
from django.db import transaction
from django.db.models import Count
from django.contrib.auth import get_user_model
from django.conf import settings
from django.utils import timezone
from html2text import html2text
from email.utils import parseaddr
from ...models import Comment, Task, TaskList

logger = logging.getLogger(__name__)


def part_decode(message):
    charset = ("ascii", "ignore")
    email_charset = message.get_content_charset()
    if email_charset:
        charset = (EMailCharset(email_charset).input_charset,)

    body = message.get_payload(decode=True)
    return body.decode(*charset)


def message_find_mime(message, mime_type):
    for submessage in message.walk():
        if submessage.get_content_type() == mime_type:
            return submessage
    return None


def message_text(message):
    text_part = message_find_mime(message, "text/plain")
    if text_part is not None:
        return part_decode(text_part)

    html_part = message_find_mime(message, "text/html")
    if html_part is not None:
        return html2text(part_decode(html_part))

    # TODO: find something smart to do when no text if found
    return ""


def message_header(message, name, default=""):
    headers = getattr(message, "headers", None)
    if headers:
        return headers.get(name) or headers.get(name.lower()) or default

    try:
        return message.get(name, default)
    except AttributeError:
        return default


def message_attr(message, attr, header=None, default=""):
    value = getattr(message, attr, None)
    if value:
        return value
    return message_header(message, header or attr, default)


def message_body(message):
    plain = getattr(message, "plain", None)
    if plain:
        return plain

    html = getattr(message, "html", None)
    if html:
        return html

    return message_text(message)


def message_datetime(message):
    value = message_attr(message, "date", "Date", None)
    if value is None:
        return timezone.now()
    if hasattr(value, "tzinfo"):
        return value

    try:
        parsed = parsedate_to_datetime(value)
    except (TypeError, ValueError):
        return timezone.now()

    if parsed.tzinfo is None:
        return timezone.make_aware(parsed, timezone.get_current_timezone())
    return parsed


def message_identifier(message):
    return (
        message_header(message, "Message-ID")
        or message_header(message, "Message-Id")
        or getattr(message, "id", "")
    )


def message_references(message):
    references = message_header(message, "References")
    in_reply_to = message_header(message, "In-Reply-To")
    thread_id = getattr(message, "thread_id", "")
    return " ".join(filter(None, [references, in_reply_to, thread_id]))


def format_task_title(format_string, message):
    return format_string.format(
        subject=message_attr(message, "subject", "Subject"),
        author=message_attr(message, "sender", "From"),
    )


DJANGO_TODO_THREAD = re.compile(r"<thread-(\d+)@(django-todo|incidents)>")


def parse_references(task_list, references):
    related_messages = []
    answer_thread = None
    for related_message in references.split():
        logger.info("checking reference: %r", related_message)
        match = re.match(DJANGO_TODO_THREAD, related_message)
        if match is None:
            related_messages.append(related_message)
            continue

        thread_id = int(match.group(1))
        new_answer_thread = Task.objects.filter(task_list=task_list, pk=thread_id).first()
        if new_answer_thread is not None:
            answer_thread = new_answer_thread

    if answer_thread is None:
        logger.info("no answer thread found in references")
    else:
        logger.info("found an answer thread: %s", str(answer_thread))
    return related_messages, answer_thread


def insert_message(task_list, message, priority, task_title_format):
    original_message_id = message_identifier(message)
    if not original_message_id:
        logger.warning("missing Message-ID, ignoring message")
        return

    message_from = message_attr(message, "sender", "From")
    if not message_from:
        logger.warning('missing "From" header, ignoring message')
        return

    message_subject = message_attr(message, "subject", "Subject")
    if not message_subject:
        logger.warning('missing "Subject" header, ignoring message')
        return

    logger.info(
        "received message:\t"
        f"[Subject: {message_subject}]\t"
        f"[Message-ID: {original_message_id}]\t"
        f"[Date: {message_attr(message, 'date', 'Date')}]\t"
        f"[To: {message_attr(message, 'recipient', 'To')}]\t"
        f"[Thread references: {message_references(message)}]\t"
        f"[From: {message_from}]"
    )

    # Due to limitations in MySQL wrt unique_together and TextField (grrr),
    # we must use a CharField rather than TextField for message_id.
    # In the unlikeley event that we get a VERY long inbound
    # message_id, truncate it to the max_length of a MySQL CharField.
    message_id = (
        (original_message_id[:252] + "...")
        if len(original_message_id) > 255
        else original_message_id
    )
    text = message_body(message)
    message_date = message_datetime(message)

    related_messages, answer_thread = parse_references(
        task_list, references=message_references(message)
    )
    author = match_user(message_from)

    # find the most relevant task to add a comment on.
    # among tasks in the selected task list, find the task having the
    # most email comments the current message references
    best_task = (
        Task.objects.filter(task_list=task_list, comment__email_message_id__in=related_messages)
        .annotate(num_comments=Count("comment"))
        .order_by("-num_comments")
        .only("id")
        .first()
    )

    # if no related comment is found but a thread message-id
    # (generated by django-todo) could be found, use it
    if best_task is None and answer_thread is not None:
        best_task = answer_thread

    with transaction.atomic():
        if best_task is None:
            best_task = Task.objects.create(
                priority=priority,
                title=format_task_title(task_title_format, message),
                task_list=task_list,
                created_by=author,
                created_date=message_date,
            )
        logger.info("using task: %r", best_task)

        comment, comment_created = Comment.objects.get_or_create(
            task=best_task,
            email_message_id=message_id,
            defaults={"email_from": message_from, "body": text, "author": author},
        )
        logger.info("created comment: %r", comment)


def tracker_consumer(
    producer, group=None, task_list_slug=None, priority=1, task_title_format="[MAIL] {subject}"
):
    task_list = TaskList.objects.get(group__name=group, slug=task_list_slug)
    for message in producer:
        try:
            insert_message(task_list, message, priority, task_title_format)
        except Exception:
            # ignore exceptions during insertion, in order to avoid
            logger.exception("got exception while inserting message")


def match_user(email):
    """ This function takes an email and checks for a registered user."""
    
    if getattr(settings, "TODO_MAIL_USER_MAPPER", True):
        try:
            # Find the first user that matches the email
            return get_user_model().objects.get(email=parseaddr(email)[1])
        except get_user_model().DoesNotExist:
            return None

    return None
