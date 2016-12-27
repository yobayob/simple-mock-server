# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_auto_20150908_1211'),
    ]

    operations = [
        migrations.CreateModel(
            name='License',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number', models.BigIntegerField(unique=True, null=True, blank=True)),
                ('created', models.DateField(default=datetime.date(2015, 9, 8))),
                ('setter_org', models.CharField(max_length=1000, null=True)),
                ('org', models.ForeignKey(to='core.Orgs')),
            ],
            options={
                'verbose_name': '\u041b\u0438\u0446\u0435\u043d\u0437\u0438\u044f',
                'verbose_name_plural': '\u041b\u0438\u0446\u0435\u043d\u0437\u0438\u0438',
            },
        ),
        migrations.CreateModel(
            name='LicenseType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=1000)),
                ('description', models.TextField(null=True, blank=True)),
            ],
            options={
                'verbose_name': '\u0422\u0438\u043f \u043b\u0438\u0446\u0435\u043d\u0437\u0438\u0438',
                'verbose_name_plural': '\u0422\u0438\u043f\u044b \u043b\u0438\u0446\u0435\u0437\u0438\u0439',
            },
        ),
        migrations.AddField(
            model_name='license',
            name='type',
            field=models.ForeignKey(to='core.LicenseType'),
        ),
    ]
