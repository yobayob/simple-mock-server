# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0053_auto_20151002_1334'),
    ]

    operations = [
        migrations.AddField(
            model_name='socialservice',
            name='have_accessible_env',
            field=models.BooleanField(default=False, verbose_name='\u041d\u0430\u043b\u0438\u0447\u0438\u0435 \u0434\u043e\u0441\u0442\u0443\u043f\u043d\u043e\u0439 \u0441\u0440\u0435\u0434\u044b'),
        ),
    ]
