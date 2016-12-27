# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models, migrations
from core.models import Profile

def create_profile(apps, schema_editor):
    for user in User.objects.all():
        if not Profile.objects.filter(user=user).exists():
            Profile.objects.create(user=user)

def reverse_func(apps, schema_editor):
	pass

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0077_auto_20151019_1528'),
    ]

    operations = [
        migrations.RunPython(create_profile, reverse_func),
    ]
