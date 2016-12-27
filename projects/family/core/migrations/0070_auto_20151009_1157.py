# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0069_auto_20151009_1149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formprovisionservice',
            name='name',
            field=models.CharField(unique=True, max_length=1000, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435'),
        ),
    ]
