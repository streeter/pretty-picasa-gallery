from django.conf import settings
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from annoying.decorators import render_to
from google.appengine.api import users
from account.decorators import login_required
from random import choice, shuffle

import logging
log = logging.getLogger('gallery.' + __name__)


@render_to('landing.html')
def landing(request):
    account = request.account
    if not account or not account.backend:
        return HttpResponseRedirect(reverse('account'))
    
    photos = account.backend.get_photos_in_album(account.homepage_album,
        account.homepage_size)
    shuffle(photos)
    for photo in photos:
        if photo['width'] > photo['height']:
            break
    
    return {'photo': {'id': photo['id'], 'album': account.homepage_album,
        'src': photo['url']}}

@render_to('album.html')
def album(request, album):
    account = request.account
    if not account or not account.backend:
        return HttpResponseRedirect(reverse('account'))
    
    photos = account.backend.get_photos_in_album(album)
    
    return {'current_album': album, 'photos': photos}


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
