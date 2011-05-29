from django.conf.urls.defaults import *

urlpatterns = patterns('about.views',
    url(r'^$', 'about', name='about'),
    url(r'^privacy/$', 'privacy', name='privacy'),
    url(r'^terms/$', 'terms', name='terms'),
)
