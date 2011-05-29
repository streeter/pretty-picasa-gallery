from django.conf.urls.defaults import *

urlpatterns = patterns('app.views',
    url(r'^login/$', 'login', name='login'),
    url(r'^logout/$', 'logout', name='logout'),
    url(r'^$', 'landing', name='landing'),
)
