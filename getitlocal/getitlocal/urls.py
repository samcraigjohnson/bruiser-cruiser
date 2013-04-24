from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'mainsite.views.homepage'),
    url(r'^login/', 'mainsite.views.login_page'),
    url(r'^stores/', include('mainsite.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

