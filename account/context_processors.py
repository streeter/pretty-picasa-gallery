from google.appengine.api import users

def auth(request):
    context = {}
    if hasattr(request, 'user'):
        context['user'] = request.user
    else:
        context['user'] = None
    
    if users.is_current_user_admin():
        context['logout_url'] = users.create_logout_url('/')
    
    if hasattr(request, 'account'):
        context['account'] = request.account
    else:
        context['account'] = None
    
    return context
