import os
import configparser
from .common import *

config = configparser.RawConfigParser()
config.read('/etc/okapi_production_settings.ini')

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config.get('secrets', 'SECRET_KEY')

# I meant to leave this as True for production. I want to know what is
# breaking on the server
DEBUG = config.get('general', 'DEBUG')

DATABASES = {
'default': {
    'ENGINE': 'django.db.backends.postgresql_psycopg2',
    'NAME': config.get('database', 'DATABASE_NAME'),
    'USER': config.get('database', 'DATABASE_USER'),
    'PASSWORD': config.get('database', 'DATABASE_PASSWORD'),
    'HOST': config.get('database', 'DATABASE_HOST'),
    'PORT': config.get('database', 'DATABASE_PORT'),
}
}

ALLOWED_HOSTS = [
        config.get('general', 'ALLOWED_HOSTS')
        ]
