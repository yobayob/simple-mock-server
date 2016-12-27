# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0022_auto_20150908_1531'),
    ]

    operations = [
        migrations.AddField(
            model_name='license',
            name='setter_date',
            field=models.DateField(null=True),
        ),
    ]
