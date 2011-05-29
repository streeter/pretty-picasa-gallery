from django.conf import settings
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from annoying.decorators import render_to
from google.appengine.api import users
from account.decorators import login_required

import logging
log = logging.getLogger('gallery.' + __name__)


@render_to('landing.html')
def landing(request):
    account = request.account
    if not account:
        return HttpResponseRedirect(reverse('account'))
    
    backend = account.backend
    
    return {}


def album(requst, album):
    account = request.account
    if not account:
        return HttpResponseRedirect(reverse('account'))
    
    return {}


def login(request):
    user = users.get_current_user()
    
    if not user:
        next = request.GET.get('next', '/')
        return HttpResponseRedirect(users.create_login_url(next))
    else:
        return HttpResponseRedirect(reverse('landing'))


def logout(request):
    user = users.get_current_user()
    if user:
        next = request.GET.get('next', '/')
        return HttpResponseRedirect(users.create_logout_url(next))
    else:
        return HttpResponseRedirect(reverse('landing'))
