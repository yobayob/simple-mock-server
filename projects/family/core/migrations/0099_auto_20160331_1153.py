# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0098_remove_patient_sex'),
    ]

    operations = [
        migrations.AlterField(
            model_name='routems',
            name='time',
            field=models.CharField(max_length=1000, verbose_name='\u0412\u0440\u0435\u043c\u044f'),
        ),
    ]
