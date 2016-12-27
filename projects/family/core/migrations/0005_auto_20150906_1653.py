# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20150906_1243'),
    ]

    operations = [
        migrations.CreateModel(
            name='MS',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=1000)),
                ('description', models.TextField(null=True, blank=True)),
                ('phone', models.CharField(max_length=1000, null=True)),
                ('address', models.CharField(max_length=1000, null=True)),
                ('mail', models.EmailField(max_length=254, null=True)),
                ('site', models.CharField(max_length=1000, null=True)),
            ],
            options={
                'verbose_name': '\u041c\u043e\u0431\u0438\u043b\u044c\u043d\u0430\u044f \u0441\u043b\u0443\u0436\u0431\u0430',
                'verbose_name_plural': '\u041c\u043e\u0431\u0438\u043b\u044c\u043d\u044b\u0435 \u0441\u043b\u0443\u0436\u0431\u044b',
            },
        ),
        migrations.CreateModel(
            name='Rcenters',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=1000)),
                ('description', models.TextField(null=True, blank=True)),
                ('phone', models.CharField(max_length=1000, null=True)),
                ('address', models.CharField(max_length=1000, null=True)),
                ('mail', models.EmailField(max_length=254, null=True)),
                ('site', models.CharField(max_length=1000, null=True)),
            ],
            options={
                'verbose_name': '\u0420\u0435\u0430\u0431\u043b\u0438\u0442\u0430\u0446\u0438\u043e\u043d\u043d\u044b\u0439 \u0446\u0435\u043d\u0442\u0440',
                'verbose_name_plural': '\u0420\u0435\u0430\u0431\u043b\u0438\u0442\u0430\u0446\u0438\u043e\u043d\u043d\u044b\u0439 \u0446\u0435\u043d\u0442\u0440',
            },
        ),
        migrations.RemoveField(
            model_name='suborgs',
            name='orgs',
        ),
        migrations.RemoveField(
            model_name='suborgs',
            name='suborgs',
        ),
        migrations.AlterModelOptions(
            name='district',
            options={'verbose_name': '\u0420\u0430\u0439\u043e\u043d', 'verbose_name_plural': '\u0420\u0430\u0439\u043e\u043d\u044b'},
        ),
        migrations.AlterModelOptions(
            name='emergency',
            options={'verbose_name': '\u042d\u043a\u0441\u0442\u0440\u0435\u043d\u043d\u044b\u044f \u0441\u043b\u0443\u0436\u0431\u0430', 'verbose_name_plural': '\u042d\u0439\u0441\u0442\u0440\u0435\u043d\u043d\u044b\u0435 \u0441\u043b\u0443\u0436\u0431\u044b'},
        ),
        migrations.AlterModelOptions(
            name='orgs',
            options={'verbose_name': '\u041e\u0440\u0433\u0430\u043d\u0438\u0437\u0430\u0446\u0438\u044f', 'verbose_name_plural': '\u041e\u0440\u0433\u0430\u043d\u0438\u0437\u0430\u0446\u0438\u0438'},
        ),
        migrations.AlterModelOptions(
            name='person',
            options={'verbose_name': '\u0421\u043f\u0435\u0446\u0438\u0430\u043b\u0438\u0441\u0442', 'verbose_name_plural': '\u0421\u043f\u0435\u0446\u0438\u0430\u043b\u0438\u0441\u0442\u044b'},
        ),
        migrations.AlterModelOptions(
            name='rhstatuses',
            options={'verbose_name': '\u0420\u0435\u0430\u0431\u043b\u0438\u0442\u0430\u0446\u0438\u043e\u043d\u043d\u044b\u0439 \u0441\u0442\u0430\u0442\u0443\u0441', 'verbose_name_plural': '\u0420\u0435\u0430\u0431\u0438\u043b\u0438\u0442\u0430\u0446\u0438\u043e\u043d\u043d\u044b\u0435 \u0441\u0442\u0430\u0442\u0443\u0441\u044b'},
        ),
        migrations.AlterModelOptions(
            name='typeorgs',
            options={'verbose_name': '\u0422\u0438\u043f \u043e\u0440\u0433\u0430\u043d\u0438\u0437\u0430\u0446\u0438\u0438', 'verbose_name_plural': '\u0422\u0438\u043f\u044b \u043e\u0440\u0433\u0430\u043d\u0438\u0437\u0430\u0446\u0438\u0439'},
        ),
        migrations.DeleteModel(
            name='SubOrgs',
        ),
        migrations.DeleteModel(
            name='TypeSubOrgs',
        ),
        migrations.AddField(
            model_name='rcenters',
            name='orgs',
            field=models.ForeignKey(to='core.Orgs'),
        ),
        migrations.AddField(
            model_name='ms',
            name='orgs',
            field=models.ForeignKey(to='core.Orgs'),
        ),
    ]
