# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0041_auto_20150922_1553'),
    ]

    operations = [
        migrations.CreateModel(
            name='SocialServiceType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=1000)),
                ('description', models.TextField(null=True, blank=True)),
            ],
            options={
                'verbose_name': '\u0422\u0438\u043f\u044b \u0441\u043e\u0446. \u0441\u043b\u0443\u0436\u0431',
                'verbose_name_plural': '\u0422\u0438\u043f\u044b \u0441\u043e\u0446. \u0441\u043b\u0443\u0436\u0431',
            },
        ),
        migrations.AddField(
            model_name='socialservice',
            name='type',
            field=models.ForeignKey(to='core.SocialServiceType', null=True),
        ),
    ]
