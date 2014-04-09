from django.conf.urls import patterns, url

from lending.views import *

urlpatterns = patterns ('',
    url(r'^$', LendingList.as_view(), name="lendings"),
    url(r'^new/(?P<book_pk>\d+)/$', NewLending.as_view(), name="new-lending"),
    url(r'^lending-added/(?P<lending_pk>\d+)/$', LendingAdded.as_view(), name="lending-added"),
    url(r'^users-current-lendings/(?P<username>\w+)/$', UsersCurrentLendings.as_view(), name="users-current-lendings"),
    url(r'^users-lendings/(?P<username>\w+)/$', UsersLendings.as_view(), name="users-lendings"),
    #url(r'^lending/(?P<pk>\d+)/$', LedningDetailView.as_view(), name="book"),
)