from django.conf.urls import url
from django.contrib import admin

from bookmark.views import *


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^bookmark/$', BookmarkLV.as_view(), name='index'),
    url(r'^bookmark/(?P<pk>\d+)/$', BookmarkDV.as_view(), name='detail'),
]
