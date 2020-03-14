from .common import *
import os

TAIGA_DOMAIN = os.environ.get("TAIGA_DOMAIN")
MEDIA_URL = "https://api-"+TAIGA_DOMAIN+"/media/"
STATIC_URL = "https://api-"+TAIGA_DOMAIN+"/static/"
SITES["front"]["scheme"] = "https"
SITES["front"]["domain"] = TAIGA_DOMAIN

SECRET_KEY = os.environ.get("SECRET_KEY")

DEBUG = os.environ.get("DEBUG", "true").lower() == "true"
PUBLIC_REGISTER_ENABLED = os.environ.get("PUBLIC_REGISTER_ENABLED", "true").lower() == "true"

DEFAULT_FROM_EMAIL = os.environ.get("FROM_EMAIL")
SERVER_EMAIL = DEFAULT_FROM_EMAIL

#CELERY_ENABLED = True

EVENTS_PUSH_BACKEND = "taiga.events.backends.rabbitmq.EventsPushBackend"
AMQP_URL = os.environ.get("AMQP_URL")
EVENTS_PUSH_BACKEND_OPTIONS = {"url": AMQP_URL}

# Uncomment and populate with proper connection parameters
# for enable email sending. EMAIL_HOST_USER should end by @domain.tld
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_USE_TLS = True
EMAIL_HOST = os.environ.get("EMAIL_HOST")
EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD")
EMAIL_PORT = int(os.environ.get("EMAIL_PORT"))

# Uncomment and populate with proper connection parameters
# for enable github login/singin.
#GITHUB_API_CLIENT_ID = "yourgithubclientid"
#GITHUB_API_CLIENT_SECRET = "yourgithubclientsecret"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ.get("POSTGRESQL_ADDON_DB", "taiga"),
        "USER": os.environ.get("POSTGRESQL_ADDON_USER", "taiga"),
        "PASSWORD": os.environ.get("POSTGRESQL_ADDON_PASSWORD", "taiga"),
        "HOST": os.environ.get("POSTGRESQL_ADDON_HOST", "localhost"),
        "PORT": os.environ.get("POSTGRESQL_ADDON_PORT", 5432),
    }
}
