# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('urly_bird', '0006_auto_20151101_0233'),
    ]

    operations = [
        migrations.RenameField(
            model_name='click',
            old_name='user',
            new_name='human',
        ),
    ]
