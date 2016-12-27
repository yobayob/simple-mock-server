# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0036_auto_20150917_0130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orgs',
            name='full_name',
            field=models.CharField(max_length=1000, null=True, verbose_name='\u041f\u043e\u043b\u043d\u043e\u0435 \u043d\u0430\u0437\u0432\u0430\u043d\u0438\u0435', blank=True),
        ),
    ]
