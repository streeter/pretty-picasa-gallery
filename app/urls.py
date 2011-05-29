from django.conf.urls.defaults import *

urlpatterns = patterns('app.views',
    url(r'^(?P<album>\w+)/$', 'album', name='album'),
    url(r'^$', 'landing', name='landing'),
)
