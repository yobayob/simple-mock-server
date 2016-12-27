# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20150906_2205'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('req', models.TextField(null=True, blank=True)),
                ('description', models.TextField(null=True, blank=True)),
                ('place', models.CharField(max_length=1000, null=True, blank=True)),
                ('terms', models.CharField(max_length=1000, null=True, blank=True)),
                ('cost', models.CharField(default='\u041d\u0435\u0438\u0437\u0432\u0435\u0441\u0442\u043d\u043e', max_length=1000, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='ServiceForm',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=1000)),
                ('description', models.TextField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='ServiceType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=1000)),
                ('description', models.TextField(null=True, blank=True)),
            ],
        ),
        migrations.RenameField(
            model_name='ms',
            old_name='orgs',
            new_name='org',
        ),
        migrations.AddField(
            model_name='service',
            name='form',
            field=models.ForeignKey(to='core.ServiceForm'),
        ),
        migrations.AddField(
            model_name='service',
            name='org',
            field=models.ForeignKey(to='core.Orgs'),
        ),
        migrations.AddField(
            model_name='service',
            name='type',
            field=models.ForeignKey(to='core.ServiceType'),
        ),
    ]
