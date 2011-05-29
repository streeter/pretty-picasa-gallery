from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('account.views',
    url(r'^login/$', 'login', name='login'),
    url(r'^logout/$', 'logout', name='logout'),
    
    url(r'^$', 'account', name='account'),
)
