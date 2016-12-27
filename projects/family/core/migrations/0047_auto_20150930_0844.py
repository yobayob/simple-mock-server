# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0046_auto_20150930_0837'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orgs',
            name='district',
            field=models.ForeignKey(verbose_name='\u0420\u0430\u0439\u043e\u043d', blank=True, to='core.District', null=True),
        ),
    ]
