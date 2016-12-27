# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20150906_2235'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ideology',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=1000)),
                ('description', models.TextField(null=True, blank=True)),
            ],
            options={
                'verbose_name': '\u041a\u043e\u043d\u0444\u0435\u0441\u0441\u0438\u044f',
                'verbose_name_plural': '\u041a\u043e\u043d\u0444\u0435\u0441\u0441\u0438\u0438',
            },
        ),
    ]
