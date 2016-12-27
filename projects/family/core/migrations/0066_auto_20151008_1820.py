# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

def forward(apps, schema_editor):
    # We can't import the Person model directly as it may be a newer
    # version than this migration expects. We use the historical version.
    SocialServiceTargetGroup = apps.get_model("core", "SocialServiceTargetGroup")
    MS = apps.get_model("core", "MS")
    SocialService = apps.get_model("core", "SocialService")
    for model in [MS, SocialService]:
        for obj in model.objects.all():
            if obj.target_group_tmp:
                obj.target_group.add(SocialServiceTargetGroup.objects.get(pk=obj.target_group_tmp))

def reverse(apps, schema_editor):
    pass

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0065_auto_20151008_1820'),
    ]

    operations = [
        migrations.RunPython(forward, reverse),
    ]
