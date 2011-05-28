from django.conf import settings
from django.contrib.auth.decorators import login_required
from annoying.decorators import render_to

import logging
log = logging.getLogger('gallery.' + __name__)


@render_to('landing.html')
def landing(request):
    return {}


@login_required
@render_to('about/privacy.html')
def privacy(request):
    return {}
