# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20150906_1238'),
    ]

    operations = [
        migrations.AddField(
            model_name='orgs',
            name='index',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='position',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
