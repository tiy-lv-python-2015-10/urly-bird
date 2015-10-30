from django.conf.urls import url
from urly_bird.views import ListBookmarks, CreateBookmark

urlpatterns = [
    url(r'^$', ListBookmarks.as_view(), name='list_bookmarks'),
    url(r'^create/$', CreateBookmark.as_view(), name='bookmark_create')
]