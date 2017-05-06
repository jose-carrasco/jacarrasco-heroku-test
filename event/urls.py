# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),    
    url(r'^event/edit/(?P<id>\d+)/$', views.event_edit, name='event_edit'),
    url(r'^event/details/(?P<id>\d+)/$', views.event_details, name='event_details'),
    url(r'^event/delete/(?P<id>\d+)/$', views.event_delete, name='event_delete'),
    url(r'^event/add', views.event_add, name='event_add'),    
]