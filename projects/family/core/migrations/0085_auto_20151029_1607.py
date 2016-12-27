# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0084_auto_20151029_1535'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ms',
            name='show_on_map',
        ),
        migrations.RemoveField(
            model_name='socialservice',
            name='show_on_map',
        ),
    ]
