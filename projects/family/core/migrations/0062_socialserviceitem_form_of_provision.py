# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0061_formprovisionservice'),
    ]

    operations = [
        migrations.AddField(
            model_name='socialserviceitem',
            name='form_of_provision',
            field=models.ForeignKey(default=1, verbose_name='\u0424\u043e\u0440\u043c\u0430 \u043e\u043a\u0430\u0437\u0430\u043d\u0438\u044f \u0443\u0441\u043b\u0443\u0433\u0438', to='core.FormProvisionService'),
            preserve_default=False,
        ),
    ]
