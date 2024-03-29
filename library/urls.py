# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url
from library.views import *


urlpatterns = patterns ('',
    url(r'^$', BookList.as_view(), name="books"),
    url(r'^author/(?P<pk>\d+)/$', AuthorsBooks.as_view(), name="author"),
    url(r'^book/(?P<pk>\d+)/$', BookDetailAndLend.as_view(), name="book"),
    url(r'^publisher/(?P<pk>\d+)/$', PublishersBooks.as_view(), name="publisher"),
    url(r'^tag/(?P<pk>\d+)/$', TagsBooks.as_view(), name="tag"),
    url(r'^category/(?P<pk>\d+)/$', CategorysBooks.as_view(), name="category"),
    url(r'^tags/$', TagsList.as_view(), name="tags"),
    url(r'^categories/$', CategoriesList.as_view(), name="categories"),
    url(r'^advanced-search/$', AdvancedSearch.as_view(), name="advanced-search"),
    url(r'^readme/$', Readme.as_view(), name="readme"),
    )