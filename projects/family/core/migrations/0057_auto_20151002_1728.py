# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0056_rehabprogram'),
    ]

    operations = [
        migrations.CreateModel(
            name='SpecialistType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=1000)),
            ],
            options={
                'verbose_name': '\u0421\u043f\u0435\u0446\u0438\u0430\u043b\u0438\u0441\u0442',
                'verbose_name_plural': '\u0421\u043f\u0435\u0446\u0438\u0430\u043b\u0438\u0441\u0442\u044b',
            },
        ),
        migrations.AddField(
            model_name='socialservice',
            name='chief',
            field=models.CharField(max_length=1000, null=True, verbose_name='\u0424\u0418\u041e \u0440\u0443\u043a\u043e\u0432\u043e\u0434\u0438\u0442\u0435\u043b\u044f \u043f\u043e\u0434\u0440\u0430\u0437\u0434\u0435\u043b\u0435\u043d\u0438\u044f', blank=True),
        ),
        migrations.AddField(
            model_name='socialservice',
            name='chief_post',
            field=models.CharField(max_length=1000, null=True, verbose_name='\u0414\u043e\u043b\u0436\u043d\u043e\u0441\u0442\u044c \u0440\u0443\u043a\u043e\u0432\u043e\u0434\u0438\u0442\u0435\u043b\u044f \u043f\u043e\u0434\u0440\u0430\u0437\u0434\u0435\u043b\u0435\u043d\u0438\u044f', blank=True),
        ),
        migrations.AddField(
            model_name='socialservice',
            name='specialist',
            field=models.ManyToManyField(to='core.SpecialistType', verbose_name='\u0421\u043f\u0435\u0446\u0438\u0430\u043b\u0438\u0441\u0442\u044b'),
        ),
    ]
