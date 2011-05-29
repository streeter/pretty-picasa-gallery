from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('account.views',
    # Examples:
    # url(r'^$', 'gallery.views.home', name='home'),
    # url(r'^gallery/', include('gallery.foo.urls')),
    
    url(r'^$', 'account', name='account'),
)
