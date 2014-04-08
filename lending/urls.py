from django.conf.urls import patterns, url

from lending.views import *

urlpatterns = patterns ('',
    url(r'^$', LendingList.as_view(), name="lendings"),
)