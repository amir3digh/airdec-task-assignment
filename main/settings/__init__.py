"""
    MODULAR SETTINGS CATALOG:

    BASE_DIR -> base_dir.py
    INSTALLED_APPS -> apps.py
    AUTH_PASSWORD_VALIDATORS, AUTH_USER_MODEL -> auth.py
    MIDDLEWARE -> middleware.py
    DATABASES, DEFAULT_AUTO_FIELD -> database.py
    LANGUAGE_CODE, TIME_ZONE, USE_I18N, USE_TZ -> internationalization.py
    TEMPLATES -> templates.py
"""
from .core import *
from .apps import *
from .middleware import *
from .templates import *
from .database import *
from .auth import *
from .internationalization import *
