"""Django Settings."""

__author__ = 'chris@chrisstreeter.com (Chris Streeter)'

import os

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

###############################################################################
## Import our defaults (globals)
from conf.default import *

###############################################################################
## Environment specific settings
DJANGO_CONF = os.environ.get('DJANGO_CONF', 'default')
if DJANGO_CONF != 'default':
    module = __import__(DJANGO_CONF, globals(), local(), ['*'])
    for k in dir(module):
        locals()[k] = getattr(module, k)

###############################################################################
## Import local settings
try:
    from local_settings import *
except ImportError, e:
    import sys
    import traceback
    sys.stderr.write("Warning: Can't find the file 'local_settings.py' in the "
            "directory containing %r. It appears you've customized things.\n"
            "You'll have to run django-admin.py, passing it your settings "
            "module.\n(If the file settings.py indeed exist, it's causing an "
            "ImportError somehow.)\n" % __file__)
    sys.stderr.write("\nFor debugging purposes, the exception was:\n\n")
    traceback.print_exc()

###############################################################################
## Remove any disabled apps
if 'DISABLED_APPS' in locals():
    INSTALLED_APPS = [k for k in INSTALLED_APPS if k not in DISABLED_APPS]

    MIDDLEWARE_CLASSES = list(MIDDLEWARE_CLASSES)
    TEMPLATE_CONTEXT_PROCESSORS = list(TEMPLATE_CONTEXT_PROCESSORS)

    for a in DISABLED_APPS:
        for x, m in enumerate(MIDDLEWARE_CLASSES):
            if m.startswith(a):
                MIDDLEWARE_CLASSES.pop(x)

        for x, m in enumerate(TEMPLATE_CONTEXT_PROCESSORS):
            if m.startswith(a):
                TEMPLATE_CONTEXT_PROCESSORS.pop(x)

###############################################################################
## All done
