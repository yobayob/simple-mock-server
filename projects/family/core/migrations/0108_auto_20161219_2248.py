# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0107_auto_20161219_2156'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blankserviceplan',
            name='status',
        ),
        migrations.AddField(
            model_name='blankservice',
            name='status',
            field=models.PositiveIntegerField(default=1, verbose_name='\u0421\u0442\u0430\u0442\u0443\u0441 \u0443\u0441\u043b\u0443\u0433\u0438', choices=[(0, '\u0423\u0441\u043b\u0443\u0433\u0430 \u043d\u0435 \u043e\u043a\u0430\u0437\u0430\u043d\u0430'), (1, '\u0423\u0441\u043b\u0443\u0433\u0430 \u043e\u043a\u0430\u0437\u0430\u043d\u0430'), (2, '\u0423\u0441\u043b\u0443\u0433\u0430 \u043e\u0442\u043c\u0435\u043d\u0435\u043d\u0430')]),
        ),
    ]
