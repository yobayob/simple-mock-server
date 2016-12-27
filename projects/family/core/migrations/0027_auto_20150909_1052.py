# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0026_auto_20150908_2103'),
    ]

    operations = [
        migrations.AddField(
            model_name='rcenters',
            name='seats',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='rcenters',
            name='seats_for_men',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='rcenters',
            name='seats_for_woman',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
