# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0049_initial_legaltypeorgs'),
    ]

    operations = [
        migrations.AddField(
            model_name='orgs',
            name='legal_type',
            field=models.ForeignKey(default=1, verbose_name='\u041e\u0440\u0433\u0430\u043d\u0438\u0437\u0430\u0446\u0438\u043e\u043d\u043d\u043e-\u043f\u0440\u0430\u0432\u043e\u0432\u0430\u044f \u0444\u043e\u0440\u043c\u0430', to='core.LegalTypeOrgs'),
        ),
    ]
