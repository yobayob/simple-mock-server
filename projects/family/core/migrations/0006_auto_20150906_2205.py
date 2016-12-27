# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20150906_1653'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='emergency',
            options={'verbose_name': '\u042d\u043a\u0441\u0442\u0440\u0435\u043d\u043d\u0430\u044f \u0441\u043b\u0443\u0436\u0431\u0430', 'verbose_name_plural': '\u042d\u043a\u0441\u0442\u0440\u0435\u043d\u043d\u044b\u0435 \u0441\u043b\u0443\u0436\u0431\u044b'},
        ),
        migrations.AlterModelOptions(
            name='rcenters',
            options={'verbose_name': '\u0420\u0435\u0430\u0431\u043b\u0438\u0442\u0430\u0446\u0438\u043e\u043d\u043d\u044b\u0439 \u0446\u0435\u043d\u0442\u0440', 'verbose_name_plural': '\u0420\u0435\u0430\u0431\u043b\u0438\u0442\u0430\u0446\u0438\u043e\u043d\u043d\u044b\u0435 \u0446\u0435\u043d\u0442\u0440\u044b'},
        ),
        migrations.RenameField(
            model_name='rcenters',
            old_name='orgs',
            new_name='org',
        ),
        migrations.AlterField(
            model_name='ms',
            name='address',
            field=models.CharField(max_length=1000, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='ms',
            name='mail',
            field=models.EmailField(max_length=254, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='ms',
            name='phone',
            field=models.CharField(max_length=1000, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='ms',
            name='site',
            field=models.CharField(max_length=1000, null=True, blank=True),
        ),
    ]
