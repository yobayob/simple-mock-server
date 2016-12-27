# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0024_auto_20150908_1538'),
    ]

    operations = [
        migrations.AddField(
            model_name='orgs',
            name='coor_x',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='orgs',
            name='coor_y',
            field=models.FloatField(null=True, blank=True),
        ),
    ]
