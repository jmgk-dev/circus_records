from .base import *

DEBUG = False

ALLOWED_HOSTS = ["146.190.150.21"]
SECRET_KEY = os.environ['DJANGO_SECRET_KEY']
DB_PASSWORD = os.environ['DJANGO_DB_PASSWORD']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'REMOVED_DB_NAME',
        'USER': 'REMOVED_DB_USER',
        'PASSWORD': 'REMOVED_DB_PASSWORD',
        'HOST': 'localhost',
        'PORT': '',
    }
}

try:
    from .local import *
except ImportError:
    pass
