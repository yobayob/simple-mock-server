# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0047_auto_20150930_0844'),
    ]

    operations = [
        migrations.CreateModel(
            name='LegalTypeOrgs',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=1000)),
            ],
            options={
                'verbose_name': '\u041e\u0440\u0433\u0430\u043d\u0438\u0437\u0430\u0446\u0438\u043e\u043d\u043d\u043e-\u043f\u0440\u0430\u0432\u043e\u0432\u0430\u044f \u0444\u043e\u0440\u043c\u0430',
                'verbose_name_plural': '\u041e\u0440\u0433\u0430\u043d\u0438\u0437\u0430\u0446\u0438\u043e\u043d\u043d\u043e-\u043f\u0440\u0430\u0432\u043e\u0432\u044b\u0435 \u0444\u043e\u0440\u043c\u044b',
            },
        ),
        migrations.AlterField(
            model_name='orgs',
            name='type',
            field=models.ForeignKey(verbose_name='\u0422\u0438\u043f \u043e\u0440\u0433\u0430\u043d\u0438\u0437\u0430\u0446\u0438\u0438', to='core.TypeOrgs'),
        ),
    ]
