from .base import *

DEBUG = False

ALLOWED_HOSTS = ["146.190.150.21"]
SECRET_KEY = os.environ['DJANGO_SECRET_KEY']


try:
    from .local import *
except ImportError:
    pass
