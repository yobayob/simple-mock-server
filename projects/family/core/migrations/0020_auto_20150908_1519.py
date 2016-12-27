# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_orgs_changed'),
    ]

    operations = [
        migrations.CreateModel(
            name='Religion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=1000)),
            ],
            options={
                'verbose_name': '\u041a\u043e\u043d\u0444\u0435\u0441\u0441\u0438\u044f',
                'verbose_name_plural': '\u041a\u043e\u043d\u0444\u0435\u0441\u0441\u0438\u0438',
            },
        ),
        migrations.DeleteModel(
            name='Emergency',
        ),
        migrations.DeleteModel(
            name='Ideology',
        ),
        migrations.RemoveField(
            model_name='person',
            name='org',
        ),
        migrations.DeleteModel(
            name='Rhstatuses',
        ),
        migrations.RemoveField(
            model_name='service',
            name='form',
        ),
        migrations.RemoveField(
            model_name='service',
            name='rcenter',
        ),
        migrations.RemoveField(
            model_name='service',
            name='type',
        ),
        migrations.DeleteModel(
            name='ServiceIndications',
        ),
        migrations.AddField(
            model_name='license',
            name='changed',
            field=models.DateField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='ms',
            name='changed',
            field=models.DateField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='ms',
            name='created',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='ms',
            name='fax',
            field=models.CharField(max_length=1000, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='orgs',
            name='chief',
            field=models.CharField(max_length=1000, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='orgs',
            name='fax',
            field=models.CharField(max_length=1000, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='rcenters',
            name='changed',
            field=models.DateField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='rcenters',
            name='created',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='rcenters',
            name='fax',
            field=models.CharField(max_length=1000, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='license',
            name='created',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.DeleteModel(
            name='Person',
        ),
        migrations.DeleteModel(
            name='Service',
        ),
        migrations.DeleteModel(
            name='ServiceForm',
        ),
        migrations.DeleteModel(
            name='ServiceType',
        ),
        migrations.AddField(
            model_name='rcenters',
            name='religion',
            field=models.ForeignKey(to='core.Religion', null=True),
        ),
    ]
