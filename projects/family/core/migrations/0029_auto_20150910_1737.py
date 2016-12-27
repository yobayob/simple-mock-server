# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0028_auto_20150909_1417'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ms',
            name='mail',
            field=models.EmailField(max_length=254, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='orgs',
            name='mail',
            field=models.EmailField(max_length=254, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='orgs',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
        migrations.AlterField(
            model_name='rcenters',
            name='mail',
            field=models.EmailField(max_length=254, null=True, blank=True),
        ),
    ]
