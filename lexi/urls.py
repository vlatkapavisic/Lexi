# -*- coding: utf-8 -*-

from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from lending.views import UsersList
from library.views import Home
from lending.forms import LexiAuthenticationForm


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', Home.as_view(), name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^books/', include('library.urls')),
    url(r'^lendings/', include('lending.urls')),
    url(r'^users/$', UsersList.as_view(), name="users"),
    url(r'^login/$', 'django.contrib.auth.views.login', 
        {'authentication_form': LexiAuthenticationForm}, name = "login" ),
    url(r'^logout/$', 'django.contrib.auth.views.logout', name = "logout"),
) 

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


