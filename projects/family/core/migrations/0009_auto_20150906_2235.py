# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20150906_2233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='rcenter',
            field=models.ForeignKey(to='core.Rcenters'),
        ),
    ]
