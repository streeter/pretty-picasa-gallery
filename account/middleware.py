from django.core.exceptions import ImproperlyConfigured
from account.models import Account

import logging
log = logging.getLogger('gallery.' + __name__)


class LazyUser(object):
    def __get__(self, request, obj_type=None):
        if not hasattr(request, '_cached_user'):
            from google.appengine.api import users
            request._cached_user = users.get_current_user()
            log.info('cached_user: %s' % request._cached_user)
        return request._cached_user


class LazyAccount(object):
    def __get__(self, request, obj_type=None):
        if not hasattr(request, '_cached_account'):
            account = Account.all().filter('user =', request.user).get()
            request._cached_account = account
            log.info('cached_account: %s' % request._cached_account)
        return request._cached_account


class AuthenticationMiddleware(object):
    def process_request(self, request):
        request.__class__.user = LazyUser()
        request.__class__.account = LazyAccount()
        return None
