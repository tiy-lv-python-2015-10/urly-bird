from django.db import models


class User(models.Model):
    anonymous = models.CharField(max_length=50)
    registration = models.CharField(max_length=50)
    log_in = models.CharField(max_length=50)
    log_out = models.CharField(max_length=50)


class UniqueCode:
    convert = models.TextField()

    @app.route('/')
    def ():
        pass


class Bookmark:
    add_bookmark = models.TextField(max_length=50)


class URL:


