
def auth(request):
    def get_user(request):
        if hasattr(request, 'user'):
            return request.user
        else:
            from django.contrib.auth.models import AnonymousUser
            return None

    return {
        'user': get_user(request),
    }
