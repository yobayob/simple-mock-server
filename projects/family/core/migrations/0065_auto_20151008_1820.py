# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0064_auto_20151008_1820'),
    ]

    operations = [
        migrations.AddField(
            model_name='ms',
            name='target_group',
            field=models.ManyToManyField(to='core.SocialServiceTargetGroup', null=True, verbose_name='\u0426\u0435\u043b\u0435\u0432\u0430\u044f \u0433\u0440\u0443\u043f\u043f\u0430', blank=True),
        ),
        migrations.AddField(
            model_name='socialservice',
            name='target_group',
            field=models.ManyToManyField(to='core.SocialServiceTargetGroup', null=True, verbose_name='\u0426\u0435\u043b\u0435\u0432\u0430\u044f \u0433\u0440\u0443\u043f\u043f\u0430', blank=True),
        ),
    ]
