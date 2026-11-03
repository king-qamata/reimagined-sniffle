"""
Django 5.0 settings for app project.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

import os
from django.core.management.utils import get_random_secret_key
from urllib.parse import urlparse
from django.contrib.messages import constants as message_constants
from django.core.exceptions import ImproperlyConfigured

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

# Note: incidents.mail modules are loaded on-demand, not at startup
# to avoid circular imports and performance issues


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", get_random_secret_key())

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv("DEBUG", "False") == "True"
#DEBUG = "True"

#ALLOWED_HOSTS = ['easy-pay-backend-f9jyg.ondigitalocean.app', '127.0.0.1']
ALLOWED_HOSTS = [
    host.strip()
    for host in os.getenv("DJANGO_ALLOWED_HOSTS", "127.0.0.1,localhost").split(",")
    if host.strip()
]
for vercel_host_variable in ("VERCEL_URL", "VERCEL_PROJECT_PRODUCTION_URL"):
    vercel_host = os.getenv(vercel_host_variable)
    if vercel_host and vercel_host not in ALLOWED_HOSTS:
        ALLOWED_HOSTS.append(vercel_host)

# Application definition

INSTALLED_APPS = [
    'dal',
    'dal_select2',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    # 'django.contrib.flatpages',  # Commented: Not used, requires django.contrib.sites
    'django.contrib.staticfiles',
    'django.contrib.sites',  # Used by incidents and other apps for domain/site management

    # REST Framework & Authentication
    'rest_framework',
    'rest_framework.authtoken',
    'drf_spectacular',  # Modern API documentation
    'drf_spectacular_sidecar',  # For schema downloads
    'dj_rest_auth',
    # 'django.contrib.sites',  # Commented: Required by allauth
    # 'allauth',  # Commented: Not currently used, enable when implementing social auth
    # 'allauth.account',
    
    # CORS & Forms
    'corsheaders',
    'crispy_forms',
    #'bootstrap5',  # Updated from bootstrap4
    
    # Extensions
    'django_extensions',
    # 'django_ratelimit',  # Commented: We use DRF throttling instead (DEFAULT_THROTTLE_CLASSES in REST_FRAMEWORK)
    
    # Project apps
    'core',
    'users',
    'filters',
    'products',
    'incidents',
    'fuelcredit',
    #'waitinglist',
    #'cohorts',
]

MIDDLEWARE = [
    # 'allauth.account.middleware.AccountMiddleware',  # Commented: Requires allauth in INSTALLED_APPS
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'app.exceptions.RequestLoggingMiddleware',  # Custom logging middleware
]

CRISPY_TEMPLATE_PACK = 'bootstrap5'  # Updated from bootstrap4

ROOT_URLCONF = 'app.urls'

AUTH_USER_MODEL = 'core.User'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "django.template.context_processors.static",
                "django.template.context_processors.tz",
            ],
        },
    },
]

WSGI_APPLICATION = 'app.wsgi.application'

# Override CSS class for the ERROR tag level to match Bootstrap class name
MESSAGE_TAGS = {message_constants.ERROR: "danger"}


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

database_url = os.getenv("DATABASE_URL")
if database_url:
    r = urlparse(database_url)
    DATABASES = {
        'default': {
            "ENGINE": "django.db.backends.postgresql_psycopg2",
            "NAME": os.path.relpath(r.path, "/"),
            "USER": r.username,
            "PASSWORD": r.password,
            "HOST": r.hostname,
            "PORT": r.port,
            "OPTIONS": {"sslmode": "require"},
        }
    }
elif os.getenv("VERCEL"):
    raise ImproperlyConfigured(
        "DATABASE_URL must be configured for Vercel deployments. "
        "SQLite is not supported as a persistent Vercel database."
    )
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }

    }


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static")
]

MEDIA_ROOT = '/vol/web/media'
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

# Caching Configuration
# Note: We use Django's locmem cache for development
# For production with multiple workers, use Redis: pip install django-redis
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'altaviz-cache',
    }
}

LOGIN_REDIRECT_URL = 'home'

LOGOUT_REDIRECT_URL = 'home'

SITE_ID = 1

# Email Configuration - Use environment variables
EMAIL_BACKEND = os.getenv(
    'EMAIL_BACKEND',
    'django.core.mail.backends.smtp.EmailBackend'
)
EMAIL_HOST = os.getenv('EMAIL_HOST', 'localhost')
EMAIL_PORT = int(os.getenv('EMAIL_PORT', '587'))
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER', '')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD', '')
EMAIL_USE_TLS = os.getenv('EMAIL_USE_TLS', 'True') == 'True'
EMAIL_USE_SSL = os.getenv('EMAIL_USE_SSL', 'False') == 'True'
DEFAULT_FROM_EMAIL = os.getenv('DEFAULT_FROM_EMAIL', EMAIL_HOST_USER or 'webmaster@localhost')

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),
    'EXCEPTION_HANDLER': 'app.exceptions.custom_exception_handler',
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 50,
    # API Documentation using drf-spectacular (modern replacement for swagger)
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
    # Rate Limiting (requests per minute)
    'DEFAULT_THROTTLE_CLASSES': [
        'rest_framework.throttling.AnonRateThrottle',
        'rest_framework.throttling.UserRateThrottle',
    ],
    'DEFAULT_THROTTLE_RATES': {
        'anon': '100/hour',  # Anonymous users: 100 requests/hour
        'user': '1000/hour',  # Authenticated users: 1000 requests/hour
    }
}

# DRF Spectacular Configuration for API Documentation
SPECTACULAR_SETTINGS = {
    'TITLE': 'Altaviz API',
    'DESCRIPTION': 'REST API for Altaviz support desk - incident tracking and ticket management',
    'VERSION': '1.0.0',
    'CONTACT': {'name': 'Altaviz Support', 'email': os.getenv('ADMIN_EMAIL', 'admin@example.com')},
    'LICENSE': {'name': 'Proprietary'},
    'SCHEMES': ['https', 'http'],
    'SERVE_PERMISSIONS': ['rest_framework.permissions.IsAuthenticated'],
    'SERVE_AUTHENTICATION': ['rest_framework.authentication.TokenAuthentication'],
    'SCHEMA_PATH_PREFIX': '/api/v1',
    'PREPROCESSING_HOOKS': ['drf_spectacular.openapi.preprocessing_filter_divisor_has_only_read_operations'],
    'SORT_OPERATION_FIELDS': False,
    'SORT_OPERATIONIDS': False,
}

ACCOUNT_USER_MODEL_USERNAME_FIELD = None
# Note: allauth is currently disabled (commented out in INSTALLED_APPS)
# Uncomment to enable social authentication:
# 1. Uncomment 'django.contrib.sites', 'allauth', 'allauth.account' in INSTALLED_APPS
# 2. Set SITE_ID = 1  
# 3. Configure allauth settings below

USER_DETAILS_SERIALIZER = 'core.serializers.user.UserSerializer'

# CORS Configuration - Use environment variables for security
CORS_ORIGIN_ALLOW_ALL = False  # Security fix: Only allow specific origins
CORS_ALLOWED_ORIGINS = [
    origin.strip() 
    for origin in os.getenv('CORS_ALLOWED_ORIGINS', 'http://localhost:3000').split(',')
]

CORS_ALLOW_HEADERS = [
    'accept',
    'accept-encoding',
    'authorization',
    'content-disposition',
    'content-type',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
]

def as_bool(value, default=False):
    if value is None:
        return default
    return str(value).strip().lower() in {"1", "true", "yes", "on"}


def env_bool(name, default=False):
    return as_bool(os.getenv(name), default)


def env_csv(name, default=""):
    return [item.strip() for item in os.getenv(name, default).split(",") if item.strip()]


def tracker_env(name, suffix, default=None):
    normalized = "".join(char if char.isalnum() else "_" for char in name.upper())
    return os.getenv(f"TODO_MAIL_TRACKER_{normalized}_{suffix}", os.getenv(f"TODO_MAIL_TRACKER_{suffix}", default))


def build_todo_mail_backends():
    """Build optional per-task-list mail backends from environment variables."""
    slugs = env_csv("TODO_MAIL_BACKEND_SLUGS", os.getenv("TODO_MAIL_LIST_SLUGS", ""))
    if not env_bool("TODO_MAIL_BACKENDS_ENABLED", bool(slugs)):
        return {}

    from incidents.mail.delivery import console_backend, locmem_backend, smtp_backend

    backend_name = os.getenv("TODO_MAIL_BACKEND", "smtp").strip().lower()
    backend_factories = {
        "smtp": smtp_backend,
        "console": console_backend,
        "locmem": locmem_backend,
    }
    backend_factory = backend_factories.get(backend_name, smtp_backend)
    from_address = os.getenv("TODO_MAIL_FROM_ADDRESS", DEFAULT_FROM_EMAIL)
    reply_to = os.getenv("TODO_MAIL_REPLY_TO", "")
    headers = {"Reply-To": reply_to} if reply_to else {}

    backend_kwargs = {"from_address": from_address, "headers": headers}
    if backend_name == "smtp":
        backend_kwargs.update(
            host=EMAIL_HOST,
            port=EMAIL_PORT,
            username=EMAIL_HOST_USER,
            password=EMAIL_HOST_PASSWORD,
            use_tls=EMAIL_USE_TLS,
            use_ssl=EMAIL_USE_SSL,
            timeout=int(os.getenv("EMAIL_TIMEOUT", "30")),
        )

    backend = backend_factory(**backend_kwargs)
    return {slug: backend for slug in (slugs or ["__default__"])}


def build_todo_mail_trackers():
    """Build incoming mail worker definitions from environment variables."""
    tracker_names = env_csv("TODO_MAIL_TRACKER_NAMES")
    if not env_bool("TODO_MAIL_TRACKERS_ENABLED", bool(tracker_names)):
        return {}

    from django.core.exceptions import ImproperlyConfigured
    from incidents.mail.consumers import tracker_consumer
    from incidents.mail.producers import imap_producer

    trackers = {}
    for name in tracker_names or ["default"]:
        group = tracker_env(name, "GROUP")
        task_list_slug = tracker_env(name, "TASK_LIST_SLUG")
        if not group or not task_list_slug:
            raise ImproperlyConfigured(
                "TODO mail trackers require TODO_MAIL_TRACKER_GROUP and "
                "TODO_MAIL_TRACKER_TASK_LIST_SLUG, or per-tracker variants."
            )

        trackers[name] = {
            "producer": imap_producer(
                process_all=as_bool(tracker_env(name, "PROCESS_ALL"), False),
                preserve=as_bool(tracker_env(name, "PRESERVE"), False),
                nap_duration=int(tracker_env(name, "NAP_DURATION", "30")),
                input_folder=tracker_env(name, "INPUT_FOLDER", "INBOX"),
                gmail_client_secret_file=tracker_env(name, "GMAIL_CLIENT_SECRET_FILE", os.getenv("GMAIL_CLIENT_SECRET_FILE", "")),
                gmail_creds_file=tracker_env(name, "GMAIL_CREDS_FILE", os.getenv("GMAIL_CREDS_FILE", "")),
                newer_than_days=int(tracker_env(name, "NEWER_THAN_DAYS", "2")),
            ),
            "consumer": tracker_consumer(
                group=group,
                task_list_slug=task_list_slug,
                priority=int(tracker_env(name, "PRIORITY", "1")),
                task_title_format=tracker_env(name, "TASK_TITLE_FORMAT", "[MAIL] {subject}"),
            ),
        }
    return trackers


# Outgoing task-notification backends and incoming mail workers.
TODO_MAIL_BACKENDS = build_todo_mail_backends()
TODO_MAIL_TRACKERS = build_todo_mail_trackers()

# Match inbound email senders to users by email address when creating tasks/comments.
TODO_MAIL_USER_MAPPER = env_bool("TODO_MAIL_USER_MAPPER", True)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        '': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}

# Enable or disable file attachments on Tasks
# Optionally limit list of allowed filetypes
TODO_ALLOW_FILE_ATTACHMENTS = True
TODO_ALLOWED_FILE_ATTACHMENTS = [".jpg", ".gif", ".csv", ".pdf", ".zip"]
TODO_MAXIMUM_ATTACHMENT_SIZE = 5000000  # In bytes
# If you use the "public" ticket filing option, to which list should these tickets be saved?
# Defaults to first list found, which is probably not what you want!
TODO_DEFAULT_LIST_SLUG = 'faultcalls'
TODO_DEFAULT_ASSIGNEE = None
TODO_STAFF_ONLY = False
