# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_auto_20150908_1245'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orgs',
            name='changed',
        ),
    ]
