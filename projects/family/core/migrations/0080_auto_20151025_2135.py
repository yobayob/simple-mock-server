# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0079_auto_20151025_2132'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField(verbose_name='\u0414\u0430\u0442\u0430 \u043f\u0440\u043e\u0432\u0435\u0434\u0435\u043d\u0438\u044f')),
                ('name', models.CharField(max_length=1000, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043c\u0435\u0440\u043e\u043f\u0440\u0438\u044f\u0442\u0438\u044f')),
                ('time', models.TimeField(verbose_name='\u0412\u0440\u0435\u043c\u044f \u043f\u0440\u043e\u0432\u0435\u0434\u0435\u043d\u0438\u044f')),
                ('address', models.TextField(verbose_name='\u041c\u0435\u0441\u0442\u043e \u043f\u0440\u043e\u0432\u0435\u0434\u0435\u043d\u0438\u044f')),
                ('participant', models.TextField(verbose_name='\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f \u0443\u0447\u0430\u0441\u0442\u043d\u0438\u043a\u043e\u0432')),
                ('description', models.TextField(null=True, verbose_name='\u0414\u043e\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044c\u043d\u0430\u044f \u0438\u043d\u0446\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f', blank=True)),
                ('created', models.DateField(auto_now_add=True, verbose_name='\u0414\u0430\u0442\u0430 \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f')),
                ('changed', models.DateField(auto_now=True, verbose_name='\u0414\u0430\u0442\u0430 \u043f\u043e\u0441\u043b\u0435\u0434\u043d\u0435\u0433\u043e \u0438\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u044f')),
                ('organization', models.ForeignKey(to='core.Orgs')),
            ],
            options={
                'verbose_name': '\u041c\u0435\u0440\u043e\u043f\u0440\u0438\u044f\u0442\u0438\u0435',
                'verbose_name_plural': '\u041c\u0435\u0440\u043e\u043f\u0440\u0438\u044f\u0442\u0438\u044f',
            },
        ),
        migrations.RemoveField(
            model_name='events',
            name='organization',
        ),
        migrations.DeleteModel(
            name='Events',
        ),
    ]
