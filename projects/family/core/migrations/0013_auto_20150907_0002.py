# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_auto_20150906_2354'),
    ]

    operations = [
        migrations.AddField(
            model_name='orgs',
            name='created',
            field=models.DateField(default=datetime.date(2015, 9, 7)),
        ),
        migrations.AddField(
            model_name='orgs',
            name='uuid',
            field=models.CharField(max_length=1000, unique=True, null=True, blank=True),
        ),
    ]
