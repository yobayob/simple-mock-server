# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0106_blankserviceplan_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='changed',
            field=models.DateField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='created',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='blankservice',
            name='date',
            field=models.DateField(default=datetime.date(2016, 12, 19), verbose_name='\u0414\u0430\u0442\u0430 \u0443\u0441\u043b\u0443\u0433\u0438'),
        ),
    ]
