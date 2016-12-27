# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_auto_20150908_1225'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='licensetype',
            options={'verbose_name': '\u0422\u0438\u043f \u043b\u0438\u0446\u0435\u043d\u0437\u0438\u0438', 'verbose_name_plural': '\u0422\u0438\u043f\u044b \u043b\u0438\u0446\u0435\u043d\u0437\u0438\u0439'},
        ),
        migrations.AddField(
            model_name='orgs',
            name='changed',
            field=models.DateField(auto_now=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='orgs',
            name='created',
            field=models.DateField(auto_now_add=True),
        ),
    ]
