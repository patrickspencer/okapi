import os
from .common import *

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Do not use 789j3kyb+yvd$^dqt8lmd%-f$dxw^_rr@oc5!wn$wg2j(6&s!3 as the
# secret key in production!
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY','789j3kyb+yvd$^dqt8lmd%-f$dxw^_rr@oc5!wn$wg2j(6&s!3')

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('DATABASE_NAME'),
        'USER': os.environ.get('DATABASE_NAME'),
        'PASSWORD': os.environ.get('DATABASE_PASSWORD'),
        'HOST': os.environ.get('DATABASE_HOST'),
        'PORT': os.environ.get('DATABASE_PORT'),
    }
}

ALLOWED_HOSTS = [host for host in os.environ.get('ALLOWED_HOSTS','localhost').split()]

