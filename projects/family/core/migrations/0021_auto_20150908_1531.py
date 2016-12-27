# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0020_auto_20150908_1519'),
    ]

    operations = [
        migrations.RenameField(
            model_name='license',
            old_name='org',
            new_name='orgs',
        ),
    ]
