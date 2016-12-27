# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0057_auto_20151002_1728'),
    ]

    operations = [
        migrations.AddField(
            model_name='ms',
            name='chief',
            field=models.CharField(max_length=1000, null=True, verbose_name='\u0424\u0418\u041e \u0440\u0443\u043a\u043e\u0432\u043e\u0434\u0438\u0442\u0435\u043b\u044f \u043f\u043e\u0434\u0440\u0430\u0437\u0434\u0435\u043b\u0435\u043d\u0438\u044f', blank=True),
        ),
        migrations.AddField(
            model_name='ms',
            name='chief_post',
            field=models.CharField(max_length=1000, null=True, verbose_name='\u0414\u043e\u043b\u0436\u043d\u043e\u0441\u0442\u044c \u0440\u0443\u043a\u043e\u0432\u043e\u0434\u0438\u0442\u0435\u043b\u044f \u043f\u043e\u0434\u0440\u0430\u0437\u0434\u0435\u043b\u0435\u043d\u0438\u044f', blank=True),
        ),
        migrations.AddField(
            model_name='ms',
            name='coor_x',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='ms',
            name='coor_y',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='ms',
            name='have_accessible_env',
            field=models.BooleanField(default=False, verbose_name='\u041d\u0430\u043b\u0438\u0447\u0438\u0435 \u0434\u043e\u0441\u0442\u0443\u043f\u043d\u043e\u0439 \u0441\u0440\u0435\u0434\u044b'),
        ),
        migrations.AddField(
            model_name='ms',
            name='have_religion_content',
            field=models.BooleanField(default=False, verbose_name='\u041d\u0430\u043b\u0438\u0447\u0438\u0435 \u0440\u0435\u043b\u0438\u0433\u0438\u043e\u0437\u043d\u043e\u0433\u043e \u0441\u043e\u0434\u0435\u0440\u0436\u0430\u043d\u0438\u044f'),
        ),
        migrations.AddField(
            model_name='ms',
            name='target_group',
            field=models.ForeignKey(verbose_name='\u0426\u0435\u043b\u0435\u0432\u0430\u044f \u0433\u0440\u0443\u043f\u043f\u0430', blank=True, to='core.SocialServiceTargetGroup', null=True),
        ),
        migrations.AddField(
            model_name='ms',
            name='type',
            field=models.ForeignKey(to='core.SocialServiceType', null=True),
        ),
        migrations.AlterField(
            model_name='ms',
            name='changed',
            field=models.DateField(default=datetime.datetime(2015, 10, 5, 13, 18, 32, 509349), auto_now=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='ms',
            name='created',
            field=models.DateField(default=datetime.datetime(2015, 10, 5, 13, 18, 39, 984978), auto_now_add=True),
            preserve_default=False,
        ),
    ]
