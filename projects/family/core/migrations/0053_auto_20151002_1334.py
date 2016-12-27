# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0052_auto_20151001_1625'),
    ]

    operations = [
        migrations.CreateModel(
            name='SocialServiceTargetGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=1000)),
            ],
            options={
                'verbose_name': '\u0426\u0435\u043b\u0435\u0432\u0430\u044f \u0433\u0440\u0443\u043f\u043f\u0430',
                'verbose_name_plural': '\u0426\u0435\u043b\u0435\u0432\u044b\u0435 \u0433\u0440\u0443\u043f\u043f\u044b',
            },
        ),
        migrations.AlterModelOptions(
            name='certificate',
            options={'verbose_name': '\u0421\u0435\u0440\u0442\u0438\u0444\u0438\u043a\u0430\u0442', 'verbose_name_plural': 'C\u0435\u0440\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u044b \u0441\u043e\u043e\u0442\u0432\u0435\u0442\u0441\u0442\u0432\u0438\u044f'},
        ),
        migrations.AddField(
            model_name='socialservice',
            name='have_religion_content',
            field=models.BooleanField(default=False, verbose_name='\u041d\u0430\u043b\u0438\u0447\u0438\u0435 \u0440\u0435\u043b\u0438\u0433\u0438\u043e\u0437\u043d\u043e\u0433\u043e \u0441\u043e\u0434\u0435\u0440\u0436\u0430\u043d\u0438\u044f'),
        ),
        migrations.AddField(
            model_name='socialservice',
            name='target_group',
            field=models.ForeignKey(verbose_name='\u0426\u0435\u043b\u0435\u0432\u0430\u044f \u0433\u0440\u0443\u043f\u043f\u0430', blank=True, to='core.SocialServiceTargetGroup', null=True),
        ),
    ]
