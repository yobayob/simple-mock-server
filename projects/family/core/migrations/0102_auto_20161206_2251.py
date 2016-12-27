# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0101_certificateforpatients_setter_org'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='position',
            field=models.CharField(max_length=1000, null=True, verbose_name='\u0414\u043e\u043b\u0436\u043d\u043e\u0441\u0442\u044c', blank=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='specialization',
            field=models.TextField(null=True, verbose_name='\u0421\u043f\u0435\u0446\u0438\u0430\u043b\u0438\u0437\u0430\u0446\u0438\u044f', blank=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='time_work',
            field=models.TextField(null=True, verbose_name='\u0412\u0440\u0435\u043c\u044f \u0440\u0430\u0431\u043e\u0442\u044b', blank=True),
        ),
    ]
