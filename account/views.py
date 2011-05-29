from django.conf import settings
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib import messages
from google.appengine.api import users
from annoying.decorators import render_to
from account.decorators import login_required
from account.models import Account
from account.forms import AccountForm

@login_required
@render_to('account/account.html')
def account(request):
    
    # Get an account object
    account = request.account
    if not account:
        account = Account(user=request.user)
        account.put()
    
    # Setup the form
    initial = {
        'photo_backend': account.photo_backend,
        'site_title': account.site_title,
        'site_header': account.site_header,
        'thumb_size': account.thumb_size,
        'thumb_cropped': account.thumb_cropped,
        'full_size': account.full_size,
        'homepage_size': account.homepage_size,
        'homepage_album': account.homepage_album,
        'featured_albums': account.featured_albums,
        'service_username': account.service_username,
        'merchant_id': account.merchant_id,
        'analytics_id': account.analytics_id,
    }
    backend = account.backend
    
    try:
        albums = backend.get_all_albums()
    except Exception, e:
        #raise e
        albums = []
    
    albums = [a['title'] for a in albums]
    
    if request.method == 'POST':
        form = AccountForm(request.POST, initial=initial)
        form.set_albums(albums)
        if form.is_valid():
            account.photo_backend = form.cleaned_data['photo_backend']
            account.site_title = form.cleaned_data['site_title']
            account.site_header = form.cleaned_data['site_header']
            account.thumb_size = form.cleaned_data['thumb_size']
            account.thumb_cropped = form.cleaned_data['thumb_cropped']
            account.full_size = form.cleaned_data['full_size']
            account.homepage_size = form.cleaned_data['homepage_size']
            account.homepage_album = form.cleaned_data['homepage_album']
            account.featured_albums = form.cleaned_data['featured_albums']
            account.service_username = form.cleaned_data['service_username']
            account.merchant_id = form.cleaned_data['merchant_id']
            account.analytics_id = form.cleaned_data['analytics_id']
            account.put()
            
            # Redirect
            messages.info(request, 'Successfully saved your account settings.')
            return HttpResponseRedirect(reverse('account'))
        messages.error(request, 'There was an error with your submission. '
            'Look for the error below.')
    else:
        form = AccountForm(initial=initial)
        form.set_albums(albums)
    
    return {'body_id': 'admin', 'title': 'Configure Your Gallery',
        'current_album': 'account', 'form': form}


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
