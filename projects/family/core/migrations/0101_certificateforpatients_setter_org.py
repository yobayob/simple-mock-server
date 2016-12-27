# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0100_auto_20160705_1449'),
    ]

    operations = [
        migrations.AddField(
            model_name='certificateforpatients',
            name='setter_org',
            field=models.ForeignKey(verbose_name='\u041d\u0430\u043f\u0440\u0430\u0432\u043b\u0435\u043d \u0438\u0437', blank=True, to='core.Orgs', null=True),
        ),
    ]
