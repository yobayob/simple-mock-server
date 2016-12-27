# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0033_initial_typeorgs'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orgs',
            name='status',
        ),
    ]
