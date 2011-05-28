from django.conf.urls.defaults import *

urlpatterns = patterns('app.views',
    url(r'^$', 'landing', name='landing'),
)
