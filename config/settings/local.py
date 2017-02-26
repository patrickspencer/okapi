import os
from .common import *

# this file is only for local development so we can keep the secret key here
SECRET_KEY = '95m0ei^4n6q(+*ty-1@=x#^%epu#6g!9y2fog#j6vs&h$rq7-h'

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
