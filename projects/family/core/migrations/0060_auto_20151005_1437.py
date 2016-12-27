# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0059_auto_20151005_1319'),
    ]

    operations = [
        migrations.CreateModel(
            name='FormProvisionService',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=1000)),
            ],
            options={
                'verbose_name': '\u0424\u043e\u0440\u043c\u0430 \u043e\u043a\u0430\u0437\u0430\u043d\u0438\u044f \u0443\u0441\u043b\u0443\u0433\u0438',
                'verbose_name_plural': '\u0424\u043e\u0440\u043c\u044b \u043e\u043a\u0430\u0437\u0430\u043d\u0438\u044f \u0443\u0441\u043b\u0443\u0433',
            },
        ),
        migrations.AddField(
            model_name='socialserviceitem',
            name='cost',
            field=models.BigIntegerField(default=0, verbose_name='\u0421\u0442\u043e\u0438\u043c\u043e\u0441\u0442\u044c (0 \u0435\u0441\u043b\u0438 \u0431\u0435\u0441\u043f\u043b\u0430\u0442\u043d\u043e)'),
        ),
        migrations.AddField(
            model_name='socialserviceitem',
            name='description',
            field=models.TextField(null=True, verbose_name='\u0414\u043e\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044c\u043d\u0430\u044f \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f', blank=True),
        ),
        migrations.AddField(
            model_name='socialserviceitem',
            name='indications',
            field=models.TextField(null=True, verbose_name='\u041f\u043e\u043a\u0430\u0437\u0430\u043d\u0438\u044f \u043a \u043d\u0430\u0437\u043d\u0430\u0447\u0435\u043d\u0438\u044e', blank=True),
        ),
        migrations.AddField(
            model_name='socialserviceitem',
            name='requirements',
            field=models.TextField(null=True, verbose_name='\u0422\u0440\u0435\u0431\u043e\u0432\u0430\u043d\u0438\u044f \u043a \u043a\u043b\u0438\u0435\u043d\u0442\u0443', blank=True),
        ),
        migrations.AddField(
            model_name='socialserviceitem',
            name='term_of_service',
            field=models.CharField(max_length=1000, null=True, verbose_name='\u0421\u0440\u043e\u043a \u043e\u043a\u0430\u0437\u0430\u043d\u0438\u044f \u0443\u0441\u043b\u0443\u0433\u0438', blank=True),
        ),
        migrations.AlterField(
            model_name='socialservice',
            name='specialist',
            field=models.ManyToManyField(to='core.SpecialistType', verbose_name='\u0421\u043f\u0435\u0446\u0438\u0430\u043b\u0438\u0441\u0442\u044b', blank=True),
        ),
    ]
