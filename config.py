""" BugisDev Base Configuration """

import os

APP_DIR = os.path.abspath(os.path.dirname(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(APP_DIR, os.pardir))

TITLE = 'BugisDev'
DESCRIPTION = 'Simple Flask Application'
AUTHOR = 'Ady Rahmat MA'
DISCUSS = None

# SECRET KEY, you should replace this
SECRET_KEY = '8a0d87868f004541a99c6f6bddf4f9d5'
ASSETS_DEBUG = False
CACHE_TYPE = 'simple'

# SECURITY CONFIG
SECURITY_REGISTERABLE = True
SECURITY_RECOVERABLE = True
SECURITY_CONFIRMABLE = False
SECURITY_TRACKABLE = True
SECURITY_PASSWORD_HASH = 'bcrypt'
# SECRET KEY, you should replace this
SECURITY_PASSWORD_SALT = 'c6a1fc37d8be45aba5ed3af48831b14c'
CSRF_ENABLED = True
# SECRET KEY, you should replace this
CSRF_SESSION_KEY = 'ad190242b1dd440584ab5324688526f0'

# DATABASE CONFIG
SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', None)
DEBUG=True