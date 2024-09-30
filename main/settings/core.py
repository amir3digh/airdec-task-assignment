"""
    Django settings for test project.
    MODULAR SETTINGS CATALOG:

    BASE_DIR -> base_dir.py
    INSTALLED_APPS -> apps.py
    AUTH_PASSWORD_VALIDATORS, AUTH_USER_MODEL -> auth.py
    MIDDLEWARE -> middleware.py
    DATABASES, DEFAULT_AUTO_FIELD -> database.py
    LANGUAGE_CODE, TIME_ZONE, USE_I18N, USE_TZ -> internationalization.py
    TEMPLATES -> templates.py
"""
import os
import sys

from main.settings.base_dir import BASE_DIR

# apps folder path changed to main/apps.
# change this setting when apps directory path changed
sys.path.insert(0, os.path.join(BASE_DIR, 'main/apps'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-2+@(n!1(s1&k_7*-jqa)=0tcn*3q8lj*y@*r)_69%*wnmff%lr'

SITE_ID = 1

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

ROOT_URLCONF = 'main.urls'

WSGI_APPLICATION = 'main.wsgi.application'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'

# console email backend for test and debugging
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

