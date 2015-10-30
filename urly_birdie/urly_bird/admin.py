from django.contrib import admin
from urly_bird.models import Bookmark


@admin.register(Bookmark)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'url', 'short_url', 'description', 'created_at')

