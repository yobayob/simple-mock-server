# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_orgs_ideology'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orgs',
            name='ideology',
            field=models.ForeignKey(to='core.Ideology'),
        ),
    ]
