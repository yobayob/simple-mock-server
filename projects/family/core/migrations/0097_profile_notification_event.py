# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0096_auto_20160225_0113'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='notification_event',
            field=models.BooleanField(default=True, verbose_name='\u041e\u043f\u043e\u0432\u0435\u0449\u0435\u043d\u0438\u044f \u043e \u043d\u043e\u0432\u044b\u0445 \u043c\u0435\u0440\u043e\u043f\u0440\u0438\u044f\u0442\u0438\u044f\u0445'),
        ),
    ]
