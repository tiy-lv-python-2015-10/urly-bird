# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('urly_bird', '0004_bookmark_homo_sapien'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookmark',
            name='short_url',
        ),
    ]
