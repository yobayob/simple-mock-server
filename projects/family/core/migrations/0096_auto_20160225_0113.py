# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0095_auto_20160202_1704'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='contact_type',
            field=models.PositiveIntegerField(verbose_name='\u0422\u0438\u043f \u043a\u043e\u043d\u0442\u0430\u043a\u0442\u043d\u043e\u0439 \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u0438', choices=[(10, '\u0422\u0435\u043b\u0435\u0444\u043e\u043d'), (20, '\u0424\u0430\u043a\u0441'), (30, '\u0421\u0430\u0439\u0442'), (40, '\u042d\u043b\u0435\u043a\u0442\u0440\u043e\u043d\u043d\u0430\u044f \u043f\u043e\u0447\u0442\u0430')]),
        ),
    ]
