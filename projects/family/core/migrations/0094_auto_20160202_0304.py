# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0093_auto_20151207_2359'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='patient',
            options={'verbose_name': '\u041a\u043b\u0438\u0435\u043d\u0442', 'verbose_name_plural': '\u041a\u043b\u0438\u0435\u043d\u0442\u044b'},
        ),
        migrations.AlterModelOptions(
            name='specialisttype',
            options={'verbose_name': '\u0421\u043f\u0435\u0446\u0438\u0430\u043b\u0438\u0441\u0442', 'verbose_name_plural': '\u0421\u043f\u0435\u0446\u0438\u0430\u043b\u0438\u0441\u0442\u044b'},
        ),
        migrations.AlterField(
            model_name='certificateforpatients',
            name='patient',
            field=models.ForeignKey(verbose_name='\u041a\u043b\u0438\u0435\u043d\u0442', to='core.Patient'),
        ),
        migrations.AlterField(
            model_name='consultation',
            name='patient',
            field=models.ForeignKey(verbose_name='\u041a\u043b\u0438\u0435\u043d\u0442', blank=True, to='core.Patient', null=True),
        ),
        migrations.AlterField(
            model_name='orgs',
            name='orgn',
            field=models.BigIntegerField(unique=True, null=True, verbose_name='\u041e\u0413\u0420\u041d', blank=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='sex',
            field=models.BooleanField(default=1, verbose_name='\u041f\u043e\u043b', choices=[(1, '\u041c\u0443\u0436\u0441\u043a\u043e\u0439'), (0, '\u0416\u0435\u043d\u0441\u043a\u0438\u0439')]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(null=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
