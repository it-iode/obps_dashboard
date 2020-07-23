"""
Example settings for local development

Use this file as a base for your local development settings and copy
it to socib_website/settings/local.py. It should not be checked into
your code repository.

"""
from obps_dashboard.settings.base import *   # pylint: disable=W0614,W0401

SECRET_KEY = 'yj6o@&vrar6^l1u68!bxumj@xr4&5)zzk!h1qw&63^&@2d3w@#'
DEBUG = True

ADMINS = (
    ('You', 'your@email'),
)
MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'obps_metrics',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

INSTALLED_APPS += (
    'django_extensions',
)
