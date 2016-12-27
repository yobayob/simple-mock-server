# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('core', '0071_typeorgs_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('contact_type', models.PositiveIntegerField(verbose_name='\u0422\u0438\u043f \u043a\u043e\u043d\u0442\u0430\u043a\u0442\u043d\u043e\u0439 \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u0438', choices=[(10, 'Phone'), (20, 'Fax'), (30, 'Internet site'), (40, 'Email')])),
                ('contact_value', models.CharField(max_length=1000, verbose_name='\u0417\u043d\u0430\u0447\u0435\u043d\u0438\u0435')),
                ('name', models.CharField(max_length=1000, null=True, verbose_name='\u041f\u043e\u0434\u0440\u043e\u0431\u043d\u043e\u0441\u0442\u0438', blank=True)),
                ('object_id', models.PositiveIntegerField()),
                ('content_type', models.ForeignKey(to='contenttypes.ContentType')),
            ],
            options={
                'verbose_name': '\u041a\u043e\u043d\u0442\u0430\u043a\u0442',
                'verbose_name_plural': '\u041a\u043e\u043d\u0442\u0430\u043a\u0442\u044b',
            },
        ),
    ]
