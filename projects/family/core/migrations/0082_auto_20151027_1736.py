# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import core.models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0081_auto_20151026_0347'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='time',
        ),
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateTimeField(verbose_name='\u0414\u0430\u0442\u0430 \u043f\u0440\u043e\u0432\u0435\u0434\u0435\u043d\u0438\u044f'),
        ),
        migrations.AlterField(
            model_name='legislation',
            name='file',
            field=models.FileField(upload_to=core.models.get_file_path, verbose_name=b'\xd1\x84\xd0\xb0\xd0\xb9\xd0\xbb'),
        ),
        migrations.AlterField(
            model_name='rehabprogram',
            name='file',
            field=models.FileField(upload_to=core.models.get_file_path, null=True, verbose_name='\u0424\u0430\u0439\u043b', blank=True),
        ),
    ]
