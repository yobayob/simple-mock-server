# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.core.management import call_command

def loadfixture(apps, schema_editor):
    call_command('loaddata', 'typeorgs.json')

def reverse(apps, schema_editor):
    pass

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0032_initial_district'),
    ]

    operations = [
        migrations.RunPython(loadfixture, reverse),
    ]
