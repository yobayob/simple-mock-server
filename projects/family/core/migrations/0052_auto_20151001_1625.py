# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0051_license_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number', models.CharField(max_length=1000, null=True, blank=True)),
                ('setter_org', models.CharField(max_length=1000, null=True)),
                ('setter_date', models.DateField(null=True, blank=True)),
                ('address', models.TextField(null=True, blank=True)),
                ('created', models.DateField(auto_now_add=True)),
                ('changed', models.DateField(auto_now=True)),
                ('org', models.ForeignKey(to='core.Orgs')),
            ],
            options={
                'verbose_name': '\u0421\u0435\u0440\u0442\u0438\u0444\u0438\u043a\u0430\u0442',
                'verbose_name_plural': '\u0422\u0438\u043f\u044b \u0441\u0435\u0440\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0432',
            },
        ),
        migrations.CreateModel(
            name='CertificateType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=1000)),
            ],
            options={
                'verbose_name': '\u0422\u0438\u043f \u0441\u0435\u0440\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u0430',
                'verbose_name_plural': '\u0422\u0438\u043f\u044b \u0441\u0435\u0440\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0432',
            },
        ),
        migrations.AddField(
            model_name='certificate',
            name='type',
            field=models.ForeignKey(to='core.CertificateType'),
        ),
    ]
