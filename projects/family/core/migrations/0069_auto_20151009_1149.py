# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0068_orgs_is_in_social_register'),
    ]

    operations = [
        migrations.AlterField(
            model_name='specialisttype',
            name='name',
            field=models.CharField(unique=True, max_length=1000, verbose_name='\u0418\u043c\u044f \u0441\u043f\u0435\u0446\u0438\u0430\u043b\u0438\u0441\u0442\u0430'),
        ),
    ]
