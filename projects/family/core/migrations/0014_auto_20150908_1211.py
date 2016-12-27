# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_auto_20150907_0002'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='orgs',
            options={'verbose_name': '\u042e\u0440\u0438\u0434\u0438\u0447\u0435\u0441\u043a\u043e\u0435 \u043b\u0438\u0446\u043e', 'verbose_name_plural': '\u042e\u0440\u0438\u0434\u0438\u0447\u0435\u0441\u043a\u0438\u0435 \u043b\u0438\u0446\u0430'},
        ),
        migrations.AlterModelOptions(
            name='serviceform',
            options={'verbose_name': '\u0424\u043e\u0440\u043c\u0430 \u043e\u043a\u0430\u0437\u0430\u043d\u0438\u044f \u0443\u0441\u043b\u0443\u0433\u0438', 'verbose_name_plural': '\u0424\u043e\u0440\u043c\u044b \u043e\u043a\u0430\u0437\u044b\u0432\u0430\u0435\u043c\u044b\u0445 \u0443\u0441\u043b\u0443\u0433'},
        ),
        migrations.AlterModelOptions(
            name='servicetype',
            options={'verbose_name': '\u0422\u0438\u043f \u0443\u0441\u043b\u0443\u0433\u0438', 'verbose_name_plural': '\u0422\u0438\u043f\u044b \u043e\u043a\u0430\u0437\u044b\u0432\u0430\u0435\u043c\u044b\u0445 \u0443\u0441\u043b\u0443\u0433'},
        ),
        migrations.RemoveField(
            model_name='orgs',
            name='ideology',
        ),
        migrations.AddField(
            model_name='orgs',
            name='inn',
            field=models.BigIntegerField(unique=True, null=True),
        ),
        migrations.AddField(
            model_name='orgs',
            name='orgn',
            field=models.BigIntegerField(unique=True, null=True),
        ),
        migrations.AlterField(
            model_name='emergency',
            name='contacts',
            field=models.CharField(max_length=1000, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='orgs',
            name='address',
            field=models.CharField(max_length=1000, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='orgs',
            name='created',
            field=models.DateField(default=datetime.date(2015, 9, 8)),
        ),
        migrations.AlterField(
            model_name='orgs',
            name='index',
            field=models.CharField(max_length=1000, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='orgs',
            name='mail',
            field=models.EmailField(max_length=254, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='orgs',
            name='phone',
            field=models.CharField(max_length=1000, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='orgs',
            name='site',
            field=models.CharField(max_length=1000, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='mail',
            field=models.EmailField(max_length=254, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='phone',
            field=models.CharField(max_length=1000, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='position',
            field=models.CharField(max_length=1000, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='rcenters',
            name='address',
            field=models.CharField(max_length=1000, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='rcenters',
            name='mail',
            field=models.EmailField(max_length=254, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='rcenters',
            name='phone',
            field=models.CharField(max_length=1000, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='rcenters',
            name='site',
            field=models.CharField(max_length=1000, null=True, blank=True),
        ),
    ]
