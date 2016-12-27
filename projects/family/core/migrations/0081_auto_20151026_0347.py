# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0080_auto_20151025_2135'),
    ]

    operations = [
        migrations.CreateModel(
            name='Legislation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=1000, verbose_name='\u041d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435 \u043d\u043e\u0440\u043c\u0430\u0442\u0438\u0432\u043d\u043e-\u043f\u0440\u0430\u0432\u043e\u0432\u043e\u0433\u043e \u0430\u043a\u0442\u0430')),
                ('date', models.DateField(verbose_name='\u0414\u0430\u0442\u0430 \u043f\u0440\u0438\u043d\u044f\u0442\u0438\u044f')),
                ('file', models.FileField(upload_to=b'', verbose_name=b'\xd1\x84\xd0\xb0\xd0\xb9\xd0\xbb')),
            ],
            options={
                'verbose_name': '\u041d\u043e\u0440\u043c\u0430\u0442\u0438\u0432\u043d\u043e-\u043f\u0440\u0430\u0432\u043e\u0432\u043e\u0439 \u0430\u043a\u0442',
                'verbose_name_plural': '\u041d\u043e\u0440\u043c\u0430\u0442\u0438\u0432\u043d\u043e-\u043f\u0440\u0430\u0432\u043e\u0432\u044b\u0435 \u0430\u043a\u0442\u044b',
            },
        ),
        migrations.CreateModel(
            name='TypeLegislation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=1000, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435')),
                ('description', models.TextField(null=True, verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435', blank=True)),
            ],
            options={
                'verbose_name': '\u0422\u0438\u043f \u043d\u043e\u0440\u043c\u0430\u0442\u0438\u0432\u043d\u043e-\u043f\u0440\u0430\u0432\u043e\u0432\u043e\u0433\u043e \u0430\u043a\u0442\u0430',
                'verbose_name_plural': '\u0422\u0438\u043f\u044b \u043d\u043e\u0440\u043c\u0430\u0442\u0438\u0432\u043d\u043e-\u043f\u0440\u0430\u0432\u043e\u0432\u044b\u0445 \u0430\u043a\u0442\u043e\u0432',
            },
        ),
        migrations.AddField(
            model_name='legislation',
            name='type_of_legislation',
            field=models.ForeignKey(verbose_name=b'\xd0\xa2\xd0\xb8\xd0\xbf \xd0\xbd\xd0\xbe\xd1\x80\xd0\xbc\xd0\xb0\xd1\x82\xd0\xb8\xd0\xb2\xd0\xbd\xd0\xbe-\xd0\xbf\xd1\x80\xd0\xb0\xd0\xb2\xd0\xbe\xd0\xb2\xd0\xbe\xd0\xb3\xd0\xbe \xd0\xb0\xd0\xba\xd1\x82\xd0\xb0', to='core.TypeLegislation'),
        ),
    ]
