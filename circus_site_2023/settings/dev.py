import os
from django.core.management.utils import get_random_secret_key

from .base import *

INSTALLED_APPS = INSTALLED_APPS + ["django_extensions"]

DEBUG = True

WAGTAILADMIN_BASE_URL = "http://127.0.0.1"

ALLOWED_HOSTS = ['localhost', '127.0.0.1']

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}

SECRET_KEY = os.getenv('DJANGO_DEV_KEY', get_random_secret_key())

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
