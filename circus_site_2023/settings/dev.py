import os
from datetime import date, timedelta
from django.core.management.utils import get_random_secret_key

from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

WAGTAILADMIN_BASE_URL = "http://127.0.0.1"

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}

SECRET_KEY = os.getenv('DJANGO_DEV_KEY', get_random_secret_key())

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ["*"]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
