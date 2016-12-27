# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0037_auto_20150917_1114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orgs',
            name='inn',
            field=models.BigIntegerField(unique=True, null=True, verbose_name='\u0418\u041d\u041d', blank=True),
        ),
        migrations.AlterField(
            model_name='orgs',
            name='orgn',
            field=models.BigIntegerField(unique=True, null=True, verbose_name='\u041e\u0420\u0413\u041d', blank=True),
        ),
    ]
