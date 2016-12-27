# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0021_auto_20150908_1531'),
    ]

    operations = [
        migrations.RenameField(
            model_name='license',
            old_name='orgs',
            new_name='org',
        ),
    ]
