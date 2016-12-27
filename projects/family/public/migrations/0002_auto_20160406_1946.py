# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='personal',
            name='thumbnail',
            field=models.ImageField(upload_to=b'', null=True, verbose_name='\u0424\u043e\u0442\u043e (\u0436\u0435\u043b\u0430\u0442\u0435\u043b\u044c\u043d\u043e 200x200)'),
        ),
        migrations.AlterField(
            model_name='flatpage',
            name='text_1',
            field=tinymce.models.HTMLField(null=True, verbose_name='\u0422\u0435\u043a\u0441\u0442 1', blank=True),
        ),
        migrations.AlterField(
            model_name='flatpage',
            name='text_2',
            field=tinymce.models.HTMLField(null=True, verbose_name='\u0422\u0435\u043a\u0441\u0442 2', blank=True),
        ),
        migrations.AlterField(
            model_name='flatpage',
            name='text_3',
            field=tinymce.models.HTMLField(null=True, verbose_name='\u0422\u0435\u043a\u0441\u0442 3', blank=True),
        ),
        migrations.AlterField(
            model_name='flatpage',
            name='type',
            field=models.PositiveIntegerField(verbose_name='\u0422\u0438\u043f \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u044b', choices=[(1, '\u0413\u043b\u0430\u0432\u043d\u0430\u044f'), (2, '\u041a\u0430\u0440\u0442\u0430'), (3, '\u041f\u043e\u0434\u0430\u0447\u0430 \u0437\u0430\u044f\u0432\u043a\u0438'), (4, '\u0421\u0442\u0440\u0430\u043d\u0438\u0446\u0430 \u043e\u0442\u0434\u0435\u043b\u0430')]),
        ),
    ]
