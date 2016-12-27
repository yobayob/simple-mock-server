# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.core.management import call_command

def migrate_contact(apps, schema_editor):
    from core.models import CONTACT_TYPE_EMAIL, CONTACT_TYPE_PHONE, CONTACT_TYPE_SITE, CONTACT_TYPE_FAX
    fields = {
        'phone': CONTACT_TYPE_PHONE,
        'fax': CONTACT_TYPE_FAX,
        'site': CONTACT_TYPE_SITE,
        'mail': CONTACT_TYPE_EMAIL,
    }
    Contact = apps.get_model("core", "Contact")
    Orgs = apps.get_model("core", "Orgs")
    SocialService = apps.get_model("core", "SocialService")
    MS = apps.get_model("core", "MS")
    ContentType = apps.get_model("contenttypes", "ContentType")
    for model in [Orgs, SocialService, MS]:
        content_type = ContentType.objects.get_for_model(model)
        for obj in model.objects.all():
            for k, v in fields.iteritems():
                value = getattr(obj, k)
                if value:
                    c = Contact(
                        content_type=content_type,
                        object_id=obj.pk,
                        contact_type=v,
                        contact_value=value,
                    )
                    c.save()

def reverse(apps, schema_editor):
    pass

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0072_contact'),
    ]

    operations = [
        migrations.RunPython(migrate_contact, reverse),
    ]
