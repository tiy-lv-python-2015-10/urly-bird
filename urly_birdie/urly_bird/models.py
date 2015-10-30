from django.contrib.auth.models import User
from django.db import models


class Bookmark(models.Model):
    title = models.CharField(max_length=60)
    url = models.URLField()
    short_url = models.CharField(max_length=50)
    description = models.TextField(max_length=700, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)


class Click(models.Model):
    user = models.ForeignKey(User)
    bookmark = models.ForeignKey(Bookmark)
    clicked_at = models.DateTimeField(auto_now_add=True)