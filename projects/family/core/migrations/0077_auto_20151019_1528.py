# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0076_auto_20151019_1344'),
    ]

    operations = [
        migrations.AddField(
            model_name='ms',
            name='show_on_map',
            field=models.BooleanField(default=True, verbose_name='\u041e\u0442\u043e\u0431\u0440\u0430\u0436\u0430\u0442\u044c \u043d\u0430 \u043a\u0430\u0440\u0442\u0435'),
        ),
        migrations.AddField(
            model_name='socialservice',
            name='show_on_map',
            field=models.BooleanField(default=True, verbose_name='\u041e\u0442\u043e\u0431\u0440\u0430\u0436\u0430\u0442\u044c \u043d\u0430 \u043a\u0430\u0440\u0442\u0435'),
        ),
    ]
