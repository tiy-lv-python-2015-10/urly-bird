# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('urly_bird', '0005_remove_bookmark_short_url'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bookmark',
            old_name='homo_sapien',
            new_name='human',
        ),
    ]
