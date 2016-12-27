# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0103_auto_20161208_2210'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlankServicePlan',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_start', models.DateField(verbose_name='\u0414\u0430\u0442\u0430 \u043d\u0430\u0447\u0430\u043b\u0430 \u043e\u0431\u0441\u043b\u0443\u0436\u0438\u0432\u0430\u043d\u0438\u044f')),
                ('date_end', models.DateField(verbose_name='\u0414\u0430\u0442\u0430 \u043e\u043a\u043e\u043d\u0447\u0430\u043d\u0438\u044f \u043e\u0431\u0441\u043b\u0443\u0436\u0438\u0432\u0430\u043d\u0438\u044f')),
                ('blank', models.ForeignKey(verbose_name='\u0423\u0447\u0435\u0442\u043d\u0430\u044f \u043a\u0430\u0440\u0442\u0430', to='core.Blank')),
            ],
            options={
                'verbose_name': '\u0423\u0441\u043b\u0443\u0433\u0430 \u0438\u0437 \u043f\u043b\u0430\u043d\u0430 \u043e\u0431\u0441\u043b\u0443\u0436\u0438\u0432\u0430\u043d\u0438\u044f \u043a\u043b\u0438\u0435\u043d\u0442\u043e\u0432',
                'verbose_name_plural': '\u041f\u043b\u0430\u043d \u043e\u0431\u0441\u043b\u0443\u0436\u0438\u0432\u0430\u043d\u0438\u044f \u043a\u043b\u0438\u0435\u043d\u0442\u043e\u0432',
            },
        ),
        migrations.RemoveField(
            model_name='blankservice',
            name='service',
        ),
        migrations.RemoveField(
            model_name='blankservice',
            name='user',
        ),
        migrations.AlterField(
            model_name='blankservice',
            name='date',
            field=models.DateField(default=datetime.date(2016, 12, 14), verbose_name='\u0414\u0430\u0442\u0430 \u0443\u0441\u043b\u0443\u0433\u0438'),
        ),
        migrations.AlterField(
            model_name='blankserviceitem',
            name='organization',
            field=models.ForeignKey(related_name='blank_services', verbose_name='\u041e\u0440\u0433\u0430\u043d\u0438\u0437\u0430\u0446\u0438\u044f', to='core.Orgs'),
        ),
        migrations.AddField(
            model_name='blankserviceplan',
            name='service',
            field=models.ForeignKey(verbose_name='\u0423\u0441\u043b\u0443\u0433\u0430', to='core.BlankServiceItem'),
        ),
        migrations.AddField(
            model_name='blankserviceplan',
            name='user',
            field=models.ForeignKey(related_name='blank_services', verbose_name='\u0421\u043f\u0435\u0446\u0438\u0430\u043b\u0438\u0441\u0442', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='blankservice',
            name='service_plan',
            field=models.ForeignKey(verbose_name='\u0423\u0441\u043b\u0443\u0433\u0430', to='core.BlankServicePlan', null=True),
        ),
    ]
