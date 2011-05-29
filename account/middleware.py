from django.core.exceptions import ImproperlyConfigured

import logging
log = logging.getLogger('gallery.' + __name__)


class LazyUser(object):
    def __get__(self, request, obj_type=None):
        if not hasattr(request, '_cached_user'):
            from google.appengine.api import users
            request._cached_user = users.get_current_user()
            log.info('cached_user: %s' % request._cached_user)
        return request._cached_user


class AuthenticationMiddleware(object):
    def process_request(self, request):
        request.__class__.user = LazyUser()
        return None
