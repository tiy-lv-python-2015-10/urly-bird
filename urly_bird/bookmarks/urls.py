from django.conf.urls import url, include, patterns
from django.contrib.auth import views as auth_views

from . import views
from bookmarks.views import ListBookMarks

urlpatterns = [
    url(r'^bookmarks/', ListBookMarks.as_view(), name="list_bookmarks"),

]
