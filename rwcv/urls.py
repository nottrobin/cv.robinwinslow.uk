from django.conf.urls import patterns, include, url

import cv.views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', cv.views.HomeView.as_view(), name='home'),
    url(r'^profiles.json$', 'profiles', name='profile'),
    url(r'^admin/', include(admin.site.urls)),
)
