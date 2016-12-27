# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0034_remove_orgs_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='orgs',
            name='status',
            field=models.IntegerField(default=1, choices=[(1, b'New'), (2, b'Approved'), (3, b'Blacklisted')]),
        ),
    ]
