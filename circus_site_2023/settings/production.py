import os
from datetime import date, timedelta

from boto3.s3.connection import S3Connection
from django.core.exceptions import SuspiciousOperation
from storages.backends.s3boto3 import S3Boto3Storage

from .base import *

DEBUG = False

ALLOWED_HOSTS = ["146.190.150.21", "0.0.0.0"]

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
    'api_key': '1546c267ada4ec3b888f8b70705cb5ee',
    'project_root': '/home/jamiek/crsite',
}

TIME_IN_A_YEAR = date.today() + timedelta(days=365)

####################################################################################################
# AWS
####################################################################################################
STORAGES = {
    "default": {
        "BACKEND": "storages.backends.s3.S3Storage",
        "OPTIONS": {
            "location": "media",
        },
    },
    "staticfiles": {
        "BACKEND": 'whitenoise.storage.CompressedManifestStaticFilesStorage',
    },
}
TIME_IN_A_YEAR = date.today() + timedelta(days=365)

AWS_HEADERS = {
    'Expires': TIME_IN_A_YEAR.strftime('%a, %d %b %Y %H:%M:%S'),
    'Cache-Control': 'max-age=2628000',
}

AWS_S3_OBJECT_PARAMETERS = {
    'Expires': TIME_IN_A_YEAR.strftime('%a, %d %b %Y %H:%M:%S'),
    'CacheControl': 'max-age=2628000',
}
MEDIA_ROOT = 'media/'

AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
AWS_S3_REGION_NAME = "sfo3"
AWS_STORAGE_BUCKET_NAME = 'circus-site-23'
AWS_S3_ENDPOINT_URL = f"https://{AWS_S3_REGION_NAME}.digitaloceanspaces.com"
AWS_S3_FILE_OVERWRITE = False
AWS_IS_GZIPPED = True
AWS_S3_SECURE_URLS = True
AWS_PRELOAD_METADATA = False
AWS_DEFAULT_ACL = 'public-read'
AWS_S3_URL_PROTOCOL = 'https:'
#MEDIA_ROOT = 'media/'
AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.{AWS_S3_REGION_NAME}.cdn.digitaloceanspaces.com'
MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/media/'
