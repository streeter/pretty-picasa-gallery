from django.conf import settings
from annoying.decorators import render_to

import logging
log = logging.getLogger('gallery.' + __name__)


@render_to('about/terms.html')
def terms(request):
    return {}


@render_to('about/privacy.html')
def privacy(request):
    return {}


@render_to('about/about.html')
def about(request):
    return {}
