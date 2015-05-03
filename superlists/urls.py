from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
     url(r'^$', 'lists.views.home_page', name='home'),
     url(r'^lists/', include('lists.urls')),
     #url(r'^lists/new$', include(admin.site.urls)),
)

