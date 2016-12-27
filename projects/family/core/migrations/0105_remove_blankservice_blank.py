# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0104_auto_20161214_2300'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blankservice',
            name='blank',
        ),
    ]
