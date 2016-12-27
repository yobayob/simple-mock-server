# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.core.management import call_command

def loadfixture(apps, schema_editor):
    call_command('loaddata', 'formprovisionservice.json')

def reverse(apps, schema_editor):
    pass

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0060_auto_20151005_1437'),
    ]

    operations = [
        migrations.RunPython(loadfixture, reverse),
    ]
