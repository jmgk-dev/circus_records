import os

from .base import *

DEBUG = False

ALLOWED_HOSTS = ["146.190.150.21"]

WAGTAILADMIN_BASE_URL = "http://146.190.150.21"

SECRET_KEY = os.environ['DJANGO_SECRET_KEY']

DB_NAME = os.environ['DB_NAME']
DB_USER = os.environ['DB_USER']
DB_PASSWORD = os.environ['DB_PASSWORD']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': DB_NAME,
        'USER': DB_USER,
        'PASSWORD': DB_PASSWORD,
        'HOST': 'localhost',
        'PORT': '',
    }
}

BUGSNAG = {
    'api_key': 'REMOVED_BUGSNAG_API_KEY',
    'project_root': '/home/jamiek/crsite',
}

try:
    from .local import *
except ImportError:
    pass
