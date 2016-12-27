# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0040_auto_20150922_1545'),
    ]

    operations = [
	migrations.RenameField('Seat', 'rcenter', 'social_service'),
    ]
