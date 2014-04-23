from django.conf.urls import patterns, include, url

from django.contrib import admin

from www.views import index, accommodations


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^accommodations/$', accommodations, name='accommodations'),
    url(r'^$', index, name='index'),
    url(r'^admin/', include(admin.site.urls)),
)
