# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0002_auto_20160406_1946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personal',
            name='phone',
            field=models.CharField(default=b'8 (812) 417-31-51', max_length=1000, verbose_name='\u0422\u0435\u043b\u0435\u0444\u043e\u043d'),
        ),
        migrations.AlterField(
            model_name='personal',
            name='thumbnail',
            field=models.ImageField(upload_to=b'personal/', null=True, verbose_name='\u0424\u043e\u0442\u043e (\u0436\u0435\u043b\u0430\u0442\u0435\u043b\u044c\u043d\u043e 200x200)', blank=True),
        ),
    ]
