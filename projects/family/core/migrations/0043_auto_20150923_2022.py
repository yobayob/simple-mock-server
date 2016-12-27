# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import colorful.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0042_auto_20150922_1609'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='socialservice',
            options={'verbose_name': '\u0421\u043e\u0446\u0438\u0430\u043b\u044c\u043d\u0430\u044f \u0441\u043b\u0443\u0436\u0431\u0430', 'verbose_name_plural': '\u0421\u043e\u0446\u0438\u0430\u043b\u044c\u043d\u044b\u0435 \u0441\u043b\u0443\u0436\u0431\u044b'},
        ),
        migrations.AddField(
            model_name='socialservicetype',
            name='color',
            field=colorful.fields.RGBColorField(default=b'0095B6'),
        ),
    ]
