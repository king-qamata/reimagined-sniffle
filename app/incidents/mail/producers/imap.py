import email
import email.parser
#import imaplib
#from googleapiclient.discovery import build
import logging
import time

#from .common import gmail_authenticate, search_messages
from .label import Label
from .gmail import Gmail
from .attachment import Attachment
from .query import construct_query
from .message import Message

from email.policy import default
from contextlib import contextmanager

logger = logging.getLogger(__name__)

 #gmail = Gmail()
def imap_check(command_tuple):
    status, ids = command_tuple
    assert status == "OK", ids

def gmail_check (conn, message):
    msg = conn.users().messages().get(userId='me', id=message['id'], format='full').execute()
    # parts can be the message body, or attachments
    payload = msg['payload']
    headers = payload.get("headers")
    parts = payload.get("parts")

@contextmanager
def imap_connect():
    # conn = imaplib.IMAP4_SSL(host=host, port=port)
    # conn.login(username, password)
    conn = gmail_authenticate()
    #imap_check(conn.list())
    try:
        yield conn
    finally:
        conn.close()


def parse_message(message):
    for response_part in message:
        if not isinstance(response_part, tuple):
            continue

        message_metadata, message_content = response_part
        email_parser = email.parser.BytesFeedParser(policy=default)
        email_parser.feed(message_content)
        return email_parser.close()


def search_message(conn, *filters):
    status, message_ids = conn.search(None, *filters)
    for message_id in message_ids[0].split():
        status, message = conn.fetch(message_id, "(RFC822)")
        yield message_id, parse_message(message)


def imap_producer(
    process_all=False,
    preserve=False,
    #host=None,
    #port=993,
    #username=None,
    #password=None,
    nap_duration=1,
    input_folder="INBOX",
    gmail_client_secret_file=None,
    gmail_creds_file=None,
    newer_than_days=2,
):
    logger.debug("starting IMAP worker")
    #imap_filter = "(ALL)" if process_all else "(UNSEEN)"
    #gmail_filter = "is:unread"
    #gmail = Gmail()
    gmail_kwargs = {}
    if gmail_client_secret_file:
        gmail_kwargs["client_secret_file"] = gmail_client_secret_file
    if gmail_creds_file:
        gmail_kwargs["creds_file"] = gmail_creds_file
    gmail = Gmail(**gmail_kwargs)

    def process_batch():
        logger.debug("starting to process batch")
        # reconnect each time to avoid repeated failures due to a lost connection
        #messages = gmail.get_unread_inbox()
        query_params_1 = {"newer_than": (newer_than_days, "day")}
        if not process_all:
            query_params_1["unread"] = True
        messages = gmail.get_unread_inbox(query=construct_query(query_params_1))
        try:
            #for message_uid, message in search_message(conn, imap_filter):
            #results = search_messages(conn, gmail_filter)
            for  message in messages :
                logger.info(f"received message {message.id}{message.subject}{message.date}{message.sender}")
                try:
                    yield message
                except Exception:
                    logger.exception(f"something went wrong while processing {message.subject}")
                    raise

                #if not preserve:
                    # tag the message for deletion
                    #gmail.store(message_uid, "+FLAGS", "\\Deleted")
            else:
                logger.debug("did not receive any message")
        finally:
            if not preserve:
                # flush deleted messages
                for message_to_read in messages:
                    message_to_read.mark_as_read()

    while True:
        try:
            yield from process_batch()
        except (GeneratorExit, KeyboardInterrupt):
            # the generator was closed, due to the consumer
            # breaking out of the loop, or an exception occuring
            raise
        except Exception:
            logger.exception("mail fetching went wrong, retrying")

        # sleep to avoid using too much resources
        # TODO: get notified when a new message arrives
        time.sleep(nap_duration)
