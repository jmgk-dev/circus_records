import os
from datetime import date, timedelta

from .base import *

DEBUG = False

ALLOWED_HOSTS = ["146.190.150.21", "0.0.0.0", 'circus-records.co.uk', 'www.circus-records.co.uk']

WAGTAILADMIN_BASE_URL = "https://circus-records.co.uk"

SECRET_KEY = os.environ['SECURE_PRODUCTION_KEY']

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
    'api_key': os.environ['BUGSNAG_API_KEY'],
    'project_root': os.environ['BUGSNAG_PROJECT_ROOT'],
}

TIME_IN_A_YEAR = date.today() + timedelta(days=365)

# Enforce HTTPS in production
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True


####################################################################################################
# EMAIL
####################################################################################################


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = os.environ['EMAIL_HOST_URL']
EMAIL_HOST_USER = os.environ['EMAIL_HOST_USER']
EMAIL_HOST_PASSWORD = os.environ['EMAIL_HOST_PASSWORD']
EMAIL_USE_TLS = True
EMAIL_PORT = 587
DEFAULT_FROM_EMAIL = 'Password Reset <passwordreset@circus-records.co.uk>'

WAGTAILADMIN_NOTIFICATION_FROM_EMAIL = DEFAULT_FROM_EMAIL


####################################################################################################
# AWS
####################################################################################################

AWS_S3_ACCESS_KEY_ID = os.environ.get('AWS_S3_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')

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


