# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url
from lending.views import *



urlpatterns = patterns ('',
    url(r'^$', LendingList.as_view(), name="lendings"),
    url(r'^add-lending/(?P<book_pk>\d+)/$', AddLending.as_view(), name="add-lending"),
    url(r'^lending-added/(?P<lending_pk>\d+)/$', LendingAdded.as_view(), name="lending-added"),
    url(r'^edit-lending/(?P<pk>\d+)/$', EditLending.as_view(), name='edit-lending'),
    url(r'^finish-lending/(?P<pk>\d+)/$', FinishLending.as_view(), name='finish-lending'),
    url(r'^users-current-lendings/(?P<username>\w+)/$', UsersCurrentLendings.as_view(), name="users-current-lendings"),
    url(r'^users-lendings/(?P<username>\w+)/$', UsersLendings.as_view(), name="users-lendings"),
    url(r'^lending/(?P<pk>\d+)/$', ViewLending.as_view(), name="view-lending"),
)