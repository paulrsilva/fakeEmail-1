from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from views import  email5
admin.autodiscover()

urlpatterns = patterns('',
    
    
    url(r'^email5/$', email5),
    # Examples:
    # url(r'^$', 'nadipopust.views.home', name='home'),
    # url(r'^nadipopust/', include('nadipopust.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
)

