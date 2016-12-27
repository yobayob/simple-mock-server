# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0073_migratecontact'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ms',
            name='fax',
        ),
        migrations.RemoveField(
            model_name='ms',
            name='mail',
        ),
        migrations.RemoveField(
            model_name='ms',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='ms',
            name='site',
        ),
        migrations.RemoveField(
            model_name='orgs',
            name='fax',
        ),
        migrations.RemoveField(
            model_name='orgs',
            name='mail',
        ),
        migrations.RemoveField(
            model_name='orgs',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='orgs',
            name='site',
        ),
        migrations.RemoveField(
            model_name='socialservice',
            name='fax',
        ),
        migrations.RemoveField(
            model_name='socialservice',
            name='mail',
        ),
        migrations.RemoveField(
            model_name='socialservice',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='socialservice',
            name='site',
        ),
    ]
