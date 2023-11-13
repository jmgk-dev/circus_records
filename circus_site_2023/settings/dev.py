import os

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

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-7zi+l^q)wq!x@#kcl9+@h*pzueeb&zkxs7snb*x1fxd#y+5p94"

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ["*"]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
