# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ditrict',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Emergency',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=1000)),
                ('description', models.TextField(null=True, blank=True)),
                ('contacts', models.CharField(max_length=1000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Orgs',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('full_name', models.CharField(unique=True, max_length=1000)),
                ('name', models.CharField(unique=True, max_length=1000)),
                ('phone', models.CharField(max_length=1000, null=True)),
                ('mail', models.EmailField(max_length=254, null=True)),
                ('description', models.TextField(null=True, blank=True)),
                ('district', models.ForeignKey(to='core.Ditrict')),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=1000)),
                ('mail', models.EmailField(max_length=254, null=True)),
                ('phone', models.CharField(max_length=1000, null=True)),
                ('org', models.ForeignKey(to='core.Orgs')),
            ],
        ),
        migrations.CreateModel(
            name='Rhstatuses',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=1000)),
                ('description', models.TextField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='SubOrgs',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=1000)),
                ('description', models.TextField(null=True, blank=True)),
                ('orgs', models.ForeignKey(to='core.Orgs')),
            ],
        ),
        migrations.CreateModel(
            name='TypeOrgs',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=1000)),
                ('description', models.TextField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='TypeSubOrgs',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=1000)),
                ('description', models.TextField(null=True, blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='suborgs',
            name='suborgs',
            field=models.ForeignKey(to='core.TypeSubOrgs'),
        ),
        migrations.AddField(
            model_name='orgs',
            name='type',
            field=models.ForeignKey(to='core.TypeOrgs'),
        ),
    ]
