from miescuela.settings import *
DEBUG=True
TEMPLATE_DEBUG=DEBUG


#TEMPLATE_LOADERS = (
#    ( 'django.template.loaders.app_directories.Loader', ('django.template.loaders.eggs.Loader',)),
#    'django.template.loaders.eggs.Loader',
#)
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
DEFAULT_FROM_EMAIL = 'erik@rivera.pro'
EMAIL_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',  # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'miescuela_geo',                      # Or path to database file if using sqlite3.
        'USER': 'geouser',                      # Not used with sqlite3.
        'PASSWORD': 'geouser',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
        'OPTIONS': {
            'autocommit': True,
        }
    }
}

TASTYPIE_FULL_DEBUG = True
TASTYPIE_DEFAULT_FORMATS = ['json', 'jsonp']
