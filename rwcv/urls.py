from django.conf.urls import patterns, include, url

import cv.views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(
        r'^$',
        cv.views.CvTemplateView.as_view(template_name='cv/index.html'),
        name='home'
    ),

    url(
        r'^roles/$',
        cv.views.CvTemplateView.as_view(template_name='cv/roles.html'),
        name='roles'
    ),

    url(
        r'^publications/$',
        cv.views.CvTemplateView.as_view(template_name='cv/publications.html'),
        name='publications'
    ),

    url(
        r'^education/$',
        cv.views.CvTemplateView.as_view(template_name='cv/education.html'),
        name='education'
    ),

    url(
        r'^about-me/$',
        cv.views.CvTemplateView.as_view(template_name='cv/about-me.html'),
        name='about_me'
    ),

    url(
        r'^client-side/$',
        cv.views.CvTemplateView.as_view(template_name='cv/client-side.html'),
        name='client_side'
    ),

    url(
        r'^server-side/$',
        cv.views.CvTemplateView.as_view(template_name='cv/server-side.html'),
        name='server_side'
    ),

    url(r'^profiles[.]json/$',cv.views.profiles,name='profiles'),
)
