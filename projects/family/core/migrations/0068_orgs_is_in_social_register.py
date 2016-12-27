# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0067_auto_20151008_1834'),
    ]

    operations = [
        migrations.AddField(
            model_name='orgs',
            name='is_in_social_register',
            field=models.BooleanField(default=False, verbose_name='\u0412\u043d\u0435\u0441\u0435\u043d\u044b \u0432 \u0440\u0435\u0435\u0441\u0442\u0440 \u043f\u043e\u0441\u0442\u0430\u0432\u0449\u0438\u043a\u043e\u0432 \u0441\u043e\u0446\u0438\u0430\u043b\u044c\u043d\u044b\u0445 \u0443\u0441\u043b\u0443\u0433'),
        ),
    ]
