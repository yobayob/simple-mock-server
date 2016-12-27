# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0083_auto_20151028_1102'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='legislation',
            name='type_of_legislation',
        ),
        migrations.DeleteModel(
            name='TypeLegislation',
        ),
    ]
