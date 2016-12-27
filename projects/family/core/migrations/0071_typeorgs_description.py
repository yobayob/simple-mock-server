# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0070_auto_20151009_1157'),
    ]

    operations = [
        migrations.AddField(
            model_name='typeorgs',
            name='description',
            field=models.TextField(null=True, blank=True),
        ),
    ]
