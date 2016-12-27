# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0030_orgs_fact_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orgs',
            name='address',
            field=models.CharField(max_length=1000, null=True, verbose_name='\u042e\u0440\u0438\u0434\u0438\u0447\u0435\u0441\u043a\u0438\u0439 \u0430\u0434\u0440\u0435\u0441', blank=True),
        ),
        migrations.AlterField(
            model_name='orgs',
            name='changed',
            field=models.DateField(auto_now=True, verbose_name='\u0418\u0437\u043c\u0435\u043d\u0435\u043d\u043e', null=True),
        ),
        migrations.AlterField(
            model_name='orgs',
            name='chief',
            field=models.CharField(max_length=1000, null=True, verbose_name='\u0424\u0418\u041e \u0440\u0443\u043a\u043e\u0432\u043e\u0434\u0438\u0442\u0435\u043b\u044f', blank=True),
        ),
        migrations.AlterField(
            model_name='orgs',
            name='coor_x',
            field=models.FloatField(null=True, verbose_name='\u041a\u043e\u043e\u0440\u0434\u0438\u043d\u0430\u0442\u044b X (\u041d\u0435 \u0442\u0440\u043e\u0433\u0430\u0442\u044c!)', blank=True),
        ),
        migrations.AlterField(
            model_name='orgs',
            name='coor_y',
            field=models.FloatField(null=True, verbose_name='\u041a\u043e\u043e\u0440\u0434\u0438\u043d\u0430\u0442\u044b \u0423 (\u041d\u0435 \u0442\u0440\u043e\u0433\u0430\u0442\u044c!)', blank=True),
        ),
        migrations.AlterField(
            model_name='orgs',
            name='created',
            field=models.DateField(auto_now_add=True, verbose_name='\u0421\u043e\u0437\u0434\u0430\u043d\u043e'),
        ),
        migrations.AlterField(
            model_name='orgs',
            name='description',
            field=models.TextField(null=True, verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435', blank=True),
        ),
        migrations.AlterField(
            model_name='orgs',
            name='district',
            field=models.ForeignKey(verbose_name='\u0420\u0430\u0439\u043e\u043d', to='core.District'),
        ),
        migrations.AlterField(
            model_name='orgs',
            name='fact_address',
            field=models.CharField(max_length=1000, null=True, verbose_name='\u0424\u0430\u043a\u0442\u0438\u0447\u0435\u0441\u043a\u0438\u0439 \u0430\u0434\u0440\u0435\u0441', blank=True),
        ),
        migrations.AlterField(
            model_name='orgs',
            name='fax',
            field=models.CharField(max_length=1000, null=True, verbose_name='\u0424\u0430\u043a\u0441', blank=True),
        ),
        migrations.AlterField(
            model_name='orgs',
            name='full_name',
            field=models.CharField(unique=True, max_length=1000, verbose_name='\u041f\u043e\u043b\u043d\u043e\u0435 \u043d\u0430\u0437\u0432\u0430\u043d\u0438\u0435'),
        ),
        migrations.AlterField(
            model_name='orgs',
            name='index',
            field=models.CharField(max_length=1000, null=True, verbose_name='\u0418\u043d\u0434\u0435\u043a\u0441', blank=True),
        ),
        migrations.AlterField(
            model_name='orgs',
            name='inn',
            field=models.BigIntegerField(unique=True, null=True, verbose_name='\u0418\u041d\u041d'),
        ),
        migrations.AlterField(
            model_name='orgs',
            name='mail',
            field=models.EmailField(max_length=254, verbose_name='E-mail'),
        ),
        migrations.AlterField(
            model_name='orgs',
            name='name',
            field=models.CharField(unique=True, max_length=1000, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435'),
        ),
        migrations.AlterField(
            model_name='orgs',
            name='orgn',
            field=models.BigIntegerField(unique=True, null=True, verbose_name='\u041e\u0420\u0413\u041d'),
        ),
        migrations.AlterField(
            model_name='orgs',
            name='phone',
            field=models.CharField(max_length=1000, verbose_name='\u0422\u0435\u043b\u0435\u0444\u043e\u043d'),
        ),
        migrations.AlterField(
            model_name='orgs',
            name='site',
            field=models.CharField(max_length=1000, null=True, verbose_name='\u041e\u0444\u0438\u0446\u0438\u0430\u043b\u044c\u043d\u044b\u0439 \u0441\u0430\u0439\u0442', blank=True),
        ),
        migrations.AlterField(
            model_name='orgs',
            name='status',
            field=models.ForeignKey(verbose_name='\u0421\u0442\u0430\u0442\u0443\u0441', to='core.StatusOrgs', null=True),
        ),
        migrations.AlterField(
            model_name='orgs',
            name='type',
            field=models.ForeignKey(verbose_name='\u041e\u0440\u0433\u0430\u043d\u0438\u0437\u0430\u0446\u0438\u043e\u043d\u043d\u043e-\u043f\u0440\u0430\u0432\u043e\u0432\u0430\u044f \u0444\u043e\u0440\u043c\u0430', to='core.TypeOrgs'),
        ),
        migrations.AlterField(
            model_name='orgs',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, verbose_name='UUID', editable=False),
        ),
    ]
