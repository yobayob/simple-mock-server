# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0063_auto_20151008_1820'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ms',
            old_name='target_group',
            new_name='target_group_tmp',
        ),
        migrations.RenameField(
            model_name='socialservice',
            old_name='target_group',
            new_name='target_group_tmp',
        ),
    ]
