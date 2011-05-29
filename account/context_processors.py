
def auth(request):
    context = {}
    if hasattr(request, 'user'):
        context['user'] = request.user
    else:
        context['user'] = None
    
    if hasattr(request, 'account'):
        context['account'] = request.account
    else:
        context['account'] = None
    
    return context
