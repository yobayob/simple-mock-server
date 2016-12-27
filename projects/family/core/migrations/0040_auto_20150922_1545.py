# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0039_auto_20150921_0801'),
    ]

    operations = [
	migrations.RenameModel('Rcenters', 'SocialService')
    ]
