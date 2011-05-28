###############################################################################
## Django settings for the project.

import os

PROJECT_ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../')
PROJECT_NAME = 'pretty gallery'

###############################################################################
## Debug Flags
DEBUG = os.environ.get('SERVER_SOFTWARE', '').startswith('Dev')
TEMPLATE_DEBUG = DEBUG

###############################################################################
## Logging
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'django.utils.log.NullHandler',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
        }
    },
    'loggers': {
        'django': {
            'handlers': ['null'],
            'propagate': True,
            'level': 'DEBUG',
        },
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': False,
        },
        'gallery': {
            'handlers': ['mail_admins', 'console'],
            'level': 'ERROR',
            'propagate': False,
        }
    }
}

###############################################################################
## Admins
ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
    ('Chris Streeter', 'chris@chrisstreeter.com'),
)

MANAGERS = ADMINS

INTERNAL_IPS = (
    '127.0.0.1',
)

###############################################################################
## Database Settings
#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.mysql',
#        'NAME': 'gallery',
#        'USER': 'gallery',
#        'PASSWORD': 'gobears',
#        'HOST': 'db',
#        'PORT': '3306',
#        'OPTIONS': {
#            'init_command': 'SET storage_engine=INNODB',
#        }
#    },
#}

###############################################################################

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Los_Angeles'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = False

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/admin-static/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'oxlum8o-ux#_m9_^^()+h+h-yds)6d)v!*jk*w!dyvj)sh8f=g'

###############################################################################
## Middleware Settings
MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.middleware.gzip.GZipMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

###############################################################################
## Common Middleware Settings
DISALLOWS_USER_AGENTS = (
)
APPEND_SLASH = False
PREPEND_WWW = False

###############################################################################
## Session Middleware Settings
SESSION_COOKIE_DOMAIN = None    # No cross domain cookies
SESSION_COOKIE_NAME = 'gallery-session'
SESSION_COOKIE_SECURE = False   # Change to True for HTTPS only cookies
#SESSION_ENGINE = 'django.contrib.sessions.backends.cache'

###############################################################################
## Message Middleware Settings
#MESSAGE_STORAGE = 'django.contrib.messages.storage.cookie.CookieStorage'
# Use cookies and fall back to sessions when the message is too big.
MESSAGE_STORAGE = 'django.contrib.messages.storage.fallback.FallbackStorage'

###############################################################################
## Template Settings
TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(PROJECT_ROOT, 'templates'),
)

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    #"django.core.context_processors.i18n",
    "django.core.context_processors.request",
    "django.core.context_processors.media",
    "django.contrib.messages.context_processors.messages",
)

###############################################################################
## Installed and Enabled Applications
INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

DISABLED_APPS = (
)

###############################################################################
## Fixtures
FIXTURE_DIRS = (
)

###############################################################################
## Cache Settings
#CACHES = {
#    'default': {
#        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
#        'LOCATION': 'gallery'
#    }
#}

###############################################################################
## Google Analytics
GA_TRACKING_CODE = ''

###############################################################################
## Authentication Settings
AUTHENTICATION_BACKENDS = (
    'account.backends.EmailAuthenticationBackend',
    #'django.contrib.auth.backends.ModelBackend',
)
LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_URL = '/logout/'
AUTH_REALM = PROJECT_NAME
AUTH_PROFILE_MODULE = 'account.Account'


###############################################################################
## Static Storage Settings
STATICFILES_DIRS = (
    ('static', os.path.join(PROJECT_ROOT, 'static')),
)
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)
STATIC_URL = '/static/'
STATIC_ROOT = ''

###############################################################################
## Other Misc Settings
DATE_FORMAT = "N j, P"
