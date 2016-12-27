# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0092_auto_20151202_0053'),
    ]

    operations = [
        migrations.CreateModel(
            name='Direction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.IntegerField(default=None, null=True, verbose_name='\u0421\u0442\u0430\u0442\u0443\u0441', choices=[(None, '\u041d\u0435\u0442 \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u0438'), (1, '\u041e\u0431\u0440\u0430\u0442\u0438\u043b\u0441\u044f'), (2, '\u041e\u0431\u0440\u0430\u0442\u0438\u043b\u0441\u044f \u0432 \u0434\u0440\u0443\u0433\u0443\u044e \u043e\u0440\u0433\u0430\u043d\u0438\u0437\u0430\u0446\u0438\u044e'), (3, '\u041e\u0442\u043c\u0435\u043d\u0435\u043d\u043e')])),
            ],
            options={
                'verbose_name': '\u041d\u0430\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u043d\u0430 \u043a\u043e\u043d\u0441\u0443\u043b\u044c\u0442\u0430\u0446\u0438\u044e',
                'verbose_name_plural': '\u041d\u0430\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u044f \u043d\u0430 \u043a\u043e\u043d\u0441\u0443\u043b\u044c\u0442\u0430\u0446\u0438\u044e',
            },
        ),
        migrations.RemoveField(
            model_name='consultation',
            name='sent_to',
        ),
        migrations.RemoveField(
            model_name='consultation',
            name='status',
        ),
        migrations.AddField(
            model_name='direction',
            name='consultation',
            field=models.ForeignKey(verbose_name=b'\xd0\x9a\xd0\xbe\xd0\xbd\xd1\x81\xd1\x83\xd0\xbb\xd1\x8c\xd1\x82\xd0\xb0\xd1\x86\xd0\xb8\xd1\x8f', to='core.Consultation'),
        ),
        migrations.AddField(
            model_name='direction',
            name='social_service',
            field=models.ForeignKey(verbose_name=b'\xd0\x9d\xd0\xb0\xd0\xbf\xd1\x80\xd0\xb0\xd0\xb2\xd0\xbb\xd0\xb5\xd0\xbd \xd0\xb2', to='core.SocialService'),
        ),
    ]
