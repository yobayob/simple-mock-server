# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0058_auto_20151005_1318'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ms',
            name='coor_x',
        ),
        migrations.RemoveField(
            model_name='ms',
            name='coor_y',
        ),
    ]
