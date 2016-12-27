# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0097_profile_notification_event'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='sex',
        ),
        migrations.AddField(
            model_name='patient',
            name='sex',
            field=models.PositiveIntegerField(default=1, verbose_name='\u041f\u043e\u043b', choices=[(1, '\u041c\u0443\u0436\u0441\u043a\u043e\u0439'), (0, '\u0416\u0435\u043d\u0441\u043a\u0438\u0439')]),
        ),
    ]
