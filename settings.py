"""Django Settings."""

__author__ = 'chris@chrisstreeter.com (Chris Streeter)'

import os

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

###############################################################################
## Import our defaults (globals)
if os.environ.get('SERVER_SOFTWARE', '').startswith('Dev'):
    from conf.dev import *
else:
    from conf.default import *

###############################################################################
## Environment specific settings
DJANGO_CONF = os.environ.get('DJANGO_CONF', 'default')
if DJANGO_CONF != 'default':
    module = __import__(DJANGO_CONF, globals(), local(), ['*'])
    for k in dir(module):
        locals()[k] = getattr(module, k)

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
