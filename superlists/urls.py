from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
     url(r'^$', 'lists.views.home_page', name='home'),
     url(r'^lists/', include('lists.urls')),
     #url(r'^lists/new$', include(admin.site.urls)),
     url(r'^login/$', 'lists.views.login', name = 'login'),
     url(r'^logout/$', 'lists.views.logout', name = 'logout'),
     url(r'^join/$', 'lists.views.join', name = 'join'),
)

