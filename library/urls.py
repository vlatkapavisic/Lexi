from django.conf.urls import patterns, url

from library.views import *

urlpatterns = patterns ('',
    url(r'^$', BookList.as_view(), name="books"),
    url(r'^author/(?P<pk>\d+)/$', AuthorsBooks.as_view(), name="author"),
    url(r'^book/(?P<pk>\d+)/$', BookDetailView.as_view(), name="book"),
    url(r'^publisher/(?P<pk>\d+)/$', PublishersBooks.as_view(), name="publisher"),
    url(r'^advanced-search/$', AdvancedSearch.as_view(), name="advanced-search"),
    )