# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0055_socialserviceitem'),
    ]

    operations = [
        migrations.CreateModel(
            name='RehabProgram',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=1000)),
                ('file', models.FileField(null=True, upload_to=b'', blank=True)),
                ('org', models.ForeignKey(to='core.Orgs')),
            ],
            options={
                'verbose_name': '\u041f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0430 \u043a\u043e\u043c\u043f\u043b\u0435\u043a\u0441\u043d\u043e\u0439 \u0440\u0435\u0430\u0431\u0438\u043b\u0438\u0442\u0430\u0446\u0438\u0438 \u0438 \u0440\u0435\u0441\u043e\u0446\u0438\u0430\u043b\u0438\u0437\u0430\u0446\u0438\u0438',
                'verbose_name_plural': '\u041f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u044b \u043a\u043e\u043c\u043f\u043b\u0435\u043a\u0441\u043d\u043e\u0439 \u0440\u0435\u0430\u0431\u0438\u043b\u0438\u0442\u0430\u0446\u0438\u0438 \u0438 \u0440\u0435\u0441\u043e\u0446\u0438\u0430\u043b\u0438\u0437\u0430\u0446\u0438\u0438',
            },
        ),
    ]
