# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20150906_1143'),
    ]

    operations = [
        migrations.AddField(
            model_name='orgs',
            name='address',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='orgs',
            name='site',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
