# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0044_auto_20150929_0959'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='orgs',
            options={'verbose_name': '\u041e\u0440\u0433\u0430\u043d\u0438\u0437\u0430\u0446\u0438\u044f', 'verbose_name_plural': '\u041e\u0440\u0433\u0430\u043d\u0438\u0437\u0430\u0446\u0438\u0438'},
        ),
        migrations.AlterModelOptions(
            name='religion',
            options={'verbose_name': '\u041a\u043e\u043d\u0444\u0435\u0441\u0441\u0438\u043e\u043d\u0430\u043b\u044c\u043d\u0430\u044f \u043f\u0440\u0438\u043d\u0430\u0434\u043b\u0435\u0436\u043d\u043e\u0441\u0442\u044c', 'verbose_name_plural': '\u041a\u043e\u043d\u0444\u0435\u0441\u0441\u0438\u043e\u043d\u0430\u043b\u044c\u043d\u0430\u044f \u043f\u0440\u0438\u043d\u0430\u0434\u043b\u0435\u0436\u043d\u043e\u0441\u0442\u0438'},
        ),
        migrations.AlterModelOptions(
            name='socialservice',
            options={'verbose_name': '\u041f\u043e\u0434\u0440\u0430\u0437\u0434\u0435\u043b\u0435\u043d\u0438\u0435', 'verbose_name_plural': '\u041f\u043e\u0434\u0440\u0430\u0437\u0434\u0435\u043b\u0435\u043d\u0438\u044f'},
        ),
        migrations.AlterModelOptions(
            name='socialservicetype',
            options={'verbose_name': '\u0422\u0438\u043f\u044b \u043f\u043e\u0434\u0440\u0430\u0437\u0434\u0435\u043b\u0435\u043d\u0438\u0439', 'verbose_name_plural': '\u0422\u0438\u043f\u044b \u043f\u043e\u0434\u0440\u0430\u0437\u0434\u0435\u043b\u0435\u043d\u0438\u0439'},
        ),
        migrations.RemoveField(
            model_name='socialservice',
            name='religion',
        ),
        migrations.AddField(
            model_name='orgs',
            name='chief_post',
            field=models.CharField(max_length=1000, null=True, verbose_name='\u0414\u043e\u043b\u0436\u043d\u043e\u0441\u0442\u044c \u0440\u0443\u043a\u043e\u0432\u043e\u0434\u0438\u0442\u0435\u043b\u044f', blank=True),
        ),
        migrations.AddField(
            model_name='orgs',
            name='history',
            field=models.TextField(null=True, verbose_name='\u0418\u0441\u0442\u043e\u0440\u0438\u044f', blank=True),
        ),
        migrations.AddField(
            model_name='orgs',
            name='religion',
            field=models.ForeignKey(verbose_name='\u041a\u043e\u043d\u0444\u0435\u0441\u0441\u0438\u043e\u043d\u0430\u043b\u044c\u043d\u0430\u044f \u043f\u0440\u0438\u043d\u0430\u0434\u043b\u0435\u0436\u043d\u043e\u0441\u0442\u044c', blank=True, to='core.Religion', null=True),
        ),
        migrations.AlterField(
            model_name='license',
            name='changed',
            field=models.DateField(default=datetime.datetime(2015, 9, 30, 8, 30, 20, 664783), auto_now=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='license',
            name='number',
            field=models.CharField(max_length=1000, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='license',
            name='setter_date',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='orgs',
            name='phone',
            field=models.CharField(max_length=1000, null=True, verbose_name='\u0422\u0435\u043b\u0435\u0444\u043e\u043d', blank=True),
        ),
    ]
