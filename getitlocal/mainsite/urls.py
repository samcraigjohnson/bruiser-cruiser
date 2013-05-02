from django.conf.urls import patterns, include, url

urlpatterns = patterns('mainsite.views',
    url(r'^profile/$', 'profile'),
    url(r'^(?P<store_display_url>\w+)/$', 'detail'),
)
