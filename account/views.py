from django.conf import settings
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from annoying.decorators import render_to
from account.decorators import login_required
from account.models import Account

@login_required
@render_to('account/account.html')
def account(request):
    
    # Get an account object
    account = request.account
    if not account:
        account = Account(user=request.user)
        account.put()
    
    return {'title': 'Setup Your Gallery'}