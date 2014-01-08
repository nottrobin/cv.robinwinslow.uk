from django.conf.urls import patterns, include, url

import cv.views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', cv.views.HomeView.as_view(), name='home'),
    url(r'^roles/$', cv.views.RolesView.as_view(), name='roles'),
    url(r'^publications/$', cv.views.PublicationsView.as_view(), name='publications'),
    url(r'^education/$', cv.views.EducationView.as_view(), name='education'),
    url(r'^about-me/$', cv.views.AboutMeView.as_view(), name='about_me'),
    url(r'^client-side/$', cv.views.ClientSideView.as_view(), name='client_side'),
    url(r'^server-side/$', cv.views.ServerSideView.as_view(), name='server_side'),
    url(r'^profiles[.]json/$', cv.views.profiles, name='profiles'),
    url(r'^admin/', include(admin.site.urls)),
)
