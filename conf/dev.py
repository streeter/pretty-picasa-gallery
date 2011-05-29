# Development environment settings

import os
from conf.default import *

PROJECT_NAME = PROJECT_NAME + ' development'

###############################################################################
## Debug Flags
DEBUG = os.environ.get('SERVER_SOFTWARE', '').startswith('Dev')
TEMPLATE_DEBUG = DEBUG

###############################################################################
## Django Toolbar
try:
    import debug_toolbar  # NOQA
except ImportError:
    pass
else:
    INSTALLED_APPS += (
        'debug_toolbar',
    )
    MIDDLEWARE_CLASSES += (
        'debug_toolbar.middleware.DebugToolbarMiddleware',
    )
    DEBUG_TOOLBAR_PANELS = (
        'debug_toolbar.panels.version.VersionDebugPanel',
        'debug_toolbar.panels.timer.TimerDebugPanel',
        'debug_toolbar.panels.settings_vars.SettingsVarsDebugPanel',
        'debug_toolbar.panels.headers.HeaderDebugPanel',
        'debug_toolbar.panels.request_vars.RequestVarsDebugPanel',
        'debug_toolbar.panels.template.TemplateDebugPanel',
        'debug_toolbar.panels.signals.SignalDebugPanel',
        'debug_toolbar.panels.logger.LoggingPanel',
    )
    DEBUG_TOOLBAR_CONFIG = {
        'INTERCEPT_REDIRECTS': False,
        'HIDE_DJANGO_SQL': True,
        'SQL_WARNING_THRESHOLD': 80,
    }

###############################################################################
## Fixtures
FIXTURE_DIRS = (
    os.path.join(PROJECT_ROOT, 'fixtures'),
) + FIXTURE_DIRS

###############################################################################
## Installed and Enabled Applications
INSTALLED_APPS += (
    #'django.contrib.admin',
    #'django.contrib.admindocs',
    
    'about',
    'app',
)

DISABLED_APPS += (
)

###############################################################################
## Template Settings
TEMPLATE_CONTEXT_PROCESSORS += (
    #'django.core.context_processors.debug',
)
