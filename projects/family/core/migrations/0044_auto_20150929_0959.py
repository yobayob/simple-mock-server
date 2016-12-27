# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0043_auto_20150923_2022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orgs',
            name='mail',
            field=models.EmailField(max_length=254, null=True, verbose_name='E-mail', blank=True),
        ),
    ]
