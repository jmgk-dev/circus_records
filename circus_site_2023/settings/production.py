from .base import *

DEBUG = False

ALLOWED_HOSTS = ["146.190.150.21"]

try:
    from .local import *
except ImportError:
    pass
