# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('urly_bird', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bookmark',
            old_name='desrciption',
            new_name='description',
        ),
    ]
