# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0038_auto_20150917_1525'),
    ]

    operations = [
        migrations.CreateModel(
            name='Seat',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('seats', models.IntegerField(null=True, blank=True)),
                ('seats_for_men', models.IntegerField(null=True, blank=True)),
                ('seats_for_woman', models.IntegerField(null=True, blank=True)),
                ('created', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name': '\u041c\u0435\u0441\u0442\u0430 \u0432 \u0440\u0435\u0430\u0431\u0438\u043b\u0438\u0442\u0430\u0446\u0438\u043e\u043d\u043d\u044b\u0445 \u0446\u0435\u043d\u0442\u0440\u0430\u0445',
                'verbose_name_plural': '\u041c\u0435\u0441\u0442\u0430 \u0432 \u0440\u0435\u0430\u0431\u0438\u043b\u0438\u0442\u0430\u0446\u0438\u043e\u043d\u043d\u044b\u0445 \u0446\u0435\u043d\u0442\u0440\u0430\u0445',
            },
        ),
        migrations.RemoveField(
            model_name='rcenters',
            name='seats',
        ),
        migrations.RemoveField(
            model_name='rcenters',
            name='seats_for_men',
        ),
        migrations.RemoveField(
            model_name='rcenters',
            name='seats_for_woman',
        ),
        migrations.AlterField(
            model_name='rcenters',
            name='changed',
            field=models.DateField(default=datetime.datetime(2015, 9, 21, 8, 1, 23, 427166), auto_now=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='rcenters',
            name='created',
            field=models.DateField(default=datetime.datetime(2015, 9, 21, 8, 1, 30, 645565), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='rcenters',
            name='religion',
            field=models.ForeignKey(blank=True, to='core.Religion', null=True),
        ),
        migrations.AddField(
            model_name='seat',
            name='rcenter',
            field=models.ForeignKey(to='core.Rcenters'),
        ),
    ]
