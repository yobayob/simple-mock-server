# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0088_socialservicetype_have_seat'),
    ]

    operations = [
        migrations.AddField(
            model_name='socialservice',
            name='seats',
            field=models.IntegerField(null=True, verbose_name='\u0412\u0441\u0435\u0433\u043e \u043c\u0435\u0441\u0442', blank=True),
        ),
        migrations.AddField(
            model_name='socialservice',
            name='seats_for_men',
            field=models.IntegerField(null=True, verbose_name='\u0412\u0441\u0435\u0433\u043e \u043c\u0435\u0441\u0442 \u0434\u043b\u044f \u043c\u0443\u0436\u0447\u0438\u043d', blank=True),
        ),
        migrations.AddField(
            model_name='socialservice',
            name='seats_for_woman',
            field=models.IntegerField(null=True, verbose_name='\u0412\u0441\u0435\u0433\u043e \u043c\u0435\u0441\u0442 \u0434\u043b\u044f \u0436\u0435\u043d\u0449\u0438\u043d', blank=True),
        ),
    ]
