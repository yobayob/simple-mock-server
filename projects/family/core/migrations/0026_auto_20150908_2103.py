# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0025_auto_20150908_1723'),
    ]

    operations = [
        migrations.CreateModel(
            name='RouteMS',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('time', models.CharField(unique=True, max_length=1000)),
                ('address', models.CharField(max_length=1000, null=True, blank=True)),
                ('description', models.TextField(null=True, blank=True)),
                ('coor_x', models.FloatField(null=True, blank=True)),
                ('coor_y', models.FloatField(null=True, blank=True)),
                ('ms', models.ForeignKey(to='core.MS')),
            ],
            options={
                'verbose_name': '\u041d\u0430\u0445\u043e\u0436\u0434\u0435\u043d\u0438\u0435 \u043c\u043e\u0431\u0438\u043b\u044c\u043d\u043e\u0439 \u0441\u043b\u0443\u0436\u0431\u044b',
                'verbose_name_plural': '\u041c\u0430\u0440\u0448\u0440\u0443\u0442 \u043c\u043e\u0431\u0438\u043b\u044c\u043d\u043e\u0439 \u0441\u043b\u0443\u0436\u0431\u044b',
            },
        ),
        migrations.AddField(
            model_name='rcenters',
            name='coor_x',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='rcenters',
            name='coor_y',
            field=models.FloatField(null=True, blank=True),
        ),
    ]
