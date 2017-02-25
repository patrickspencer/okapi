import os
from .common import *

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '95m0ei^4n6q(+*ty-1@=x#^%epu#6g!9y2fog#j6vs&h$rq7-h'

# I meant to leave this as True for production. I want to know what is
# breaking on the server
DEBUG = True

DATABASES = {
'default': {
    'ENGINE': 'django.db.backends.postgresql_psycopg2',
    'NAME': 'okapi_db',
    'USER': 'okapi',
    'PASSWORD': 'password',
    'HOST': 'localhost',
    'PORT': '',
}
}
