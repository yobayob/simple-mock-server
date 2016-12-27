# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0089_auto_20151102_1036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='routems',
            name='coor_x',
            field=models.FloatField(null=True, verbose_name='\u041a\u043e\u043e\u0440\u0434\u0438\u043d\u0430\u0442\u044b X (\u041d\u0435 \u0442\u0440\u043e\u0433\u0430\u0442\u044c!)', blank=True),
        ),
        migrations.AlterField(
            model_name='routems',
            name='coor_y',
            field=models.FloatField(null=True, verbose_name='\u041a\u043e\u043e\u0440\u0434\u0438\u043d\u0430\u0442\u044b \u0423 (\u041d\u0435 \u0442\u0440\u043e\u0433\u0430\u0442\u044c!)', blank=True),
        ),
        migrations.AlterField(
            model_name='socialservice',
            name='coor_x',
            field=models.FloatField(null=True, verbose_name='\u041a\u043e\u043e\u0440\u0434\u0438\u043d\u0430\u0442\u044b X (\u041d\u0435 \u0442\u0440\u043e\u0433\u0430\u0442\u044c!)', blank=True),
        ),
        migrations.AlterField(
            model_name='socialservice',
            name='coor_y',
            field=models.FloatField(null=True, verbose_name='\u041a\u043e\u043e\u0440\u0434\u0438\u043d\u0430\u0442\u044b \u0423 (\u041d\u0435 \u0442\u0440\u043e\u0433\u0430\u0442\u044c!)', blank=True),
        ),
    ]
