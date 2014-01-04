from django.conf.urls import patterns, include, url

import cv.views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', cv.views.HomeView.as_view(), name='home'),
    url(r'^profiles[.]json$', cv.views.profiles, name='profiles'),
    url(r'^admin/', include(admin.site.urls)),
)
