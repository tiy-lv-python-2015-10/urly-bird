# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('urly_bird', '0007_auto_20151101_0507'),
    ]

    operations = [
        migrations.AlterField(
            model_name='click',
            name='human',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True, blank=True),
        ),
    ]
