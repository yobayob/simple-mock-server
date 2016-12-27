# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import colorful.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0085_auto_20151029_1607'),
    ]

    operations = [
        migrations.AddField(
            model_name='typeorgs',
            name='color',
            field=colorful.fields.RGBColorField(default=b'0095B6', verbose_name='\u0426\u0432\u0435\u0442 \u043c\u0435\u0442\u043a\u0438'),
        ),
    ]
