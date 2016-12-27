# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0045_auto_20150930_0830'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='licensetype',
            name='description',
        ),
        migrations.RemoveField(
            model_name='typeorgs',
            name='description',
        ),
    ]
