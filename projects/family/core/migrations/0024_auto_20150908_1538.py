# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0023_license_setter_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='StatusOrgs',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=1000)),
                ('description', models.TextField(null=True, blank=True)),
            ],
            options={
                'verbose_name': '\u0421\u0442\u0430\u0442\u0443\u0441 \u043e\u0440\u0433\u0430\u043d\u0438\u0437\u0430\u0446\u0438\u0438',
                'verbose_name_plural': '\u0421\u0442\u0430\u0442\u0443\u0441\u044b \u043e\u0440\u0433\u0430\u043d\u0438\u0437\u0430\u0446\u0438\u0439',
            },
        ),
        migrations.AddField(
            model_name='orgs',
            name='status',
            field=models.ForeignKey(to='core.StatusOrgs', null=True),
        ),
    ]
