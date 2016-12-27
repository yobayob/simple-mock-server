# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0075_merge'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='orgs',
        ),
        migrations.AddField(
            model_name='profile',
            name='organization',
            field=models.ForeignKey(blank=True, to='core.Orgs', null=True),
        ),
    ]
