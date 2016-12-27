# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0050_orgs_legal_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='license',
            name='address',
            field=models.TextField(null=True, blank=True),
        ),
    ]
