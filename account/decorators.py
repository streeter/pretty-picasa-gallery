try:
    from functools import wraps
except ImportError:
    from django.utils.functional import wraps  # Python 2.4 fallback.

from django.core.urlresolvers import reverse
from django.utils.decorators import available_attrs
from django.http import HttpResponseRedirect
from google.appengine.api import users


def login_required(function=None):
    
    def decorator(view_func):
        @wraps(view_func, assigned=available_attrs(view_func))
        def _wrapped_view(request, *args, **kwargs):
            if users.get_current_user():
                return view_func(request, *args, **kwargs)
            return HttpResponseRedirect(users.create_login_url(request.path))
        return _wrapped_view
    
    if function:
        return decorator(function)
    return decorator
