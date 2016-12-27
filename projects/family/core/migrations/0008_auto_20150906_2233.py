# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20150906_2224'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceIndications',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=1000)),
                ('description', models.TextField(null=True, blank=True)),
            ],
            options={
                'verbose_name': '\u041f\u043e\u043a\u0430\u0437\u0430\u043d\u0438\u044f \u043a \u043e\u043a\u0430\u0437\u0430\u043d\u0438\u044e \u0443\u0441\u043b\u0443\u0433\u0438',
                'verbose_name_plural': '\u041f\u043e\u043a\u0430\u0437\u0430\u043d\u0438\u044f \u043a \u043e\u043a\u0430\u0437\u0430\u043d\u0438\u044e \u0443\u0441\u043b\u0443\u0433',
            },
        ),
        migrations.AlterModelOptions(
            name='service',
            options={'verbose_name': '\u0423\u0441\u043b\u0443\u0433\u0430', 'verbose_name_plural': '\u0423\u0441\u043b\u0443\u0433\u0438'},
        ),
        migrations.AlterModelOptions(
            name='serviceform',
            options={'verbose_name': '\u0424\u043e\u0440\u043c\u0430 \u043e\u043a\u0430\u0437\u0430\u043d\u0438\u044f \u0443\u0441\u043b\u0443\u0433\u0438', 'verbose_name_plural': '\u0424\u043e\u0440\u043c\u044b \u043e\u043a\u0430\u0437\u0430\u043d\u0438\u044f \u0443\u0441\u043b\u0443\u0433'},
        ),
        migrations.AlterModelOptions(
            name='servicetype',
            options={'verbose_name': '\u0422\u0438\u043f \u0443\u0441\u043b\u0443\u0433\u0438', 'verbose_name_plural': '\u0422\u0438\u043f\u044b \u0443\u0441\u043b\u0443\u0433\u0438'},
        ),
        migrations.RemoveField(
            model_name='service',
            name='org',
        ),
        migrations.AddField(
            model_name='service',
            name='rcenter',
            field=models.ForeignKey(to='core.Rcenters', null=True),
        ),
    ]
