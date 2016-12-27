# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0029_auto_20150910_1737'),
    ]

    operations = [
        migrations.AddField(
            model_name='orgs',
            name='fact_address',
            field=models.CharField(max_length=1000, null=True, blank=True),
        ),
    ]
