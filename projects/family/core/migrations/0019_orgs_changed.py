# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_remove_orgs_changed'),
    ]

    operations = [
        migrations.AddField(
            model_name='orgs',
            name='changed',
            field=models.DateField(auto_now=True, null=True),
        ),
    ]
