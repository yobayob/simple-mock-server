# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FlatPage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=1000, verbose_name='title')),
                ('text_1', tinymce.models.HTMLField(verbose_name='\u0422\u0435\u043a\u0441\u0442 1')),
                ('text_2', tinymce.models.HTMLField(verbose_name='\u0422\u0435\u043a\u0441\u0442 2')),
                ('text_3', tinymce.models.HTMLField(verbose_name='\u0422\u0435\u043a\u0441\u0442 3')),
                ('type', models.PositiveIntegerField(verbose_name='\u0422\u0438\u043f \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u044b', choices=[(1, '\u0413\u043b\u0430\u0432\u043d\u0430\u044f'), (2, '\u041a\u0430\u0440\u0442\u0430'), (3, '\u041f\u043e\u0434\u0430\u0447\u0430 \u0437\u0430\u044f\u0432\u043a\u0438')])),
            ],
            options={
                'verbose_name': '\u0421\u0442\u0430\u0442\u0438\u0447\u043d\u0430\u044f \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u0430',
                'verbose_name_plural': '\u0421\u0442\u0430\u0442\u0438\u0447\u043d\u044b\u0435 \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u044b',
            },
        ),
        migrations.CreateModel(
            name='Personal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=1000, verbose_name='\u0424\u0418\u041e')),
                ('position', models.PositiveIntegerField(verbose_name='\u0414\u043e\u043b\u0436\u043d\u043e\u0441\u0442\u044c', choices=[(1, '\u041d\u0430\u0447\u0430\u043b\u044c\u043d\u0438\u043a \u043e\u0442\u0434\u0435\u043b\u0430'), (2, '\u041c\u0435\u0442\u043e\u0434\u0438\u0441\u0442'), (3, '\u041f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0438\u0441\u0442')])),
                ('phone', models.CharField(max_length=1000, verbose_name='\u0422\u0435\u043b\u0435\u0444\u043e\u043d')),
                ('mail', models.EmailField(default=b'depeduspb@gmail.com', max_length=254, verbose_name='\u041f\u043e\u0447\u0442\u0430')),
            ],
            options={
                'ordering': ['position'],
                'verbose_name': '\u041f\u0435\u0440\u0441\u043e\u043d\u0430\u043b',
                'verbose_name_plural': '\u041f\u0435\u0440\u0441\u043e\u043d\u0430\u043b',
            },
        ),
    ]
