# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import colorful.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0062_socialserviceitem_form_of_provision'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='religion',
            options={'verbose_name': '\u041a\u043e\u043d\u0444\u0435\u0441\u0441\u0438\u043e\u043d\u0430\u043b\u044c\u043d\u0430\u044f \u043f\u0440\u0438\u043d\u0430\u0434\u043b\u0435\u0436\u043d\u043e\u0441\u0442\u044c', 'verbose_name_plural': '\u041a\u043e\u043d\u0444\u0435\u0441\u0441\u0438\u043e\u043d\u0430\u043b\u044c\u043d\u044b\u0435 \u043f\u0440\u0438\u043d\u0430\u0434\u043b\u0435\u0436\u043d\u043e\u0441\u0442\u0438'},
        ),
        migrations.AlterField(
            model_name='certificate',
            name='address',
            field=models.TextField(null=True, verbose_name='\u0410\u0434\u0440\u0435\u0441\u0430 \u0434\u0435\u0439\u0441\u0442\u0432\u0438\u044f', blank=True),
        ),
        migrations.AlterField(
            model_name='certificate',
            name='changed',
            field=models.DateField(auto_now=True, verbose_name='\u0418\u0437\u043c\u0435\u043d\u0435\u043d\u043e'),
        ),
        migrations.AlterField(
            model_name='certificate',
            name='created',
            field=models.DateField(auto_now_add=True, verbose_name='\u0421\u043e\u0437\u0434\u0430\u043d\u043e'),
        ),
        migrations.AlterField(
            model_name='certificate',
            name='number',
            field=models.CharField(max_length=1000, null=True, verbose_name='\u041d\u043e\u043c\u0435\u0440', blank=True),
        ),
        migrations.AlterField(
            model_name='certificate',
            name='org',
            field=models.ForeignKey(verbose_name='\u041e\u0440\u0433\u0430\u043d\u0438\u0437\u0430\u0446\u0438\u044f', to='core.Orgs'),
        ),
        migrations.AlterField(
            model_name='certificate',
            name='setter_date',
            field=models.DateField(null=True, verbose_name='\u0414\u0430\u0442\u0430 \u0432\u044b\u0434\u0430\u0447\u0438', blank=True),
        ),
        migrations.AlterField(
            model_name='certificate',
            name='setter_org',
            field=models.CharField(max_length=1000, null=True, verbose_name='\u041e\u0440\u0433\u0430\u043d\u0438\u0437\u0430\u0446\u0438\u044f, \u0432\u044b\u0434\u0430\u0432\u0448\u0430\u044f \u0441\u0435\u0440\u0442\u0438\u0444\u0438\u043a\u0430\u0442'),
        ),
        migrations.AlterField(
            model_name='certificate',
            name='type',
            field=models.ForeignKey(verbose_name='\u0422\u0438\u043f \u0441\u0435\u0440\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u0430', to='core.CertificateType'),
        ),
        migrations.AlterField(
            model_name='certificatetype',
            name='name',
            field=models.CharField(unique=True, max_length=1000, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435'),
        ),
        migrations.AlterField(
            model_name='district',
            name='name',
            field=models.CharField(unique=True, max_length=1000, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435'),
        ),
        migrations.AlterField(
            model_name='formprovisionservice',
            name='name',
            field=models.CharField(max_length=1000, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435'),
        ),
        migrations.AlterField(
            model_name='legaltypeorgs',
            name='name',
            field=models.CharField(unique=True, max_length=1000, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435'),
        ),
        migrations.AlterField(
            model_name='license',
            name='address',
            field=models.TextField(null=True, verbose_name='\u0410\u0434\u0440\u0435\u0441\u0430 \u0434\u0435\u0439\u0441\u0442\u0432\u0438\u044f', blank=True),
        ),
        migrations.AlterField(
            model_name='license',
            name='changed',
            field=models.DateField(auto_now=True, verbose_name='\u0414\u0430\u0442\u0430 \u043f\u043e\u0441\u043b\u0435\u0434\u043d\u0435\u0433\u043e \u0438\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u044f'),
        ),
        migrations.AlterField(
            model_name='license',
            name='created',
            field=models.DateField(auto_now_add=True, verbose_name='\u0414\u0430\u0442\u0430 \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f'),
        ),
        migrations.AlterField(
            model_name='license',
            name='number',
            field=models.CharField(max_length=1000, null=True, verbose_name='\u041d\u043e\u043c\u0435\u0440 \u043b\u0438\u0446\u0435\u043d\u0437\u0438\u0438', blank=True),
        ),
        migrations.AlterField(
            model_name='license',
            name='org',
            field=models.ForeignKey(verbose_name='\u041e\u0440\u0433\u0430\u043d\u0438\u0437\u0430\u0446\u0438\u044f', to='core.Orgs'),
        ),
        migrations.AlterField(
            model_name='license',
            name='setter_date',
            field=models.DateField(null=True, verbose_name='\u0414\u0430\u0442\u0430 \u0432\u044b\u0434\u0430\u0447\u0438', blank=True),
        ),
        migrations.AlterField(
            model_name='license',
            name='setter_org',
            field=models.CharField(max_length=1000, null=True, verbose_name='\u041e\u0440\u0433\u0430\u043d\u0438\u0437\u0430\u0446\u0438\u044f, \u0432\u044b\u0434\u0430\u0432\u0448\u0430\u044f \u0441\u0435\u0440\u0442\u0438\u0444\u0438\u043a\u0430\u0442'),
        ),
        migrations.AlterField(
            model_name='license',
            name='type',
            field=models.ForeignKey(verbose_name='\u0422\u0438\u043f \u043b\u0438\u0446\u0435\u043d\u0437\u0438\u0438', to='core.LicenseType'),
        ),
        migrations.AlterField(
            model_name='licensetype',
            name='name',
            field=models.CharField(unique=True, max_length=1000, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435'),
        ),
        migrations.AlterField(
            model_name='ms',
            name='address',
            field=models.CharField(max_length=1000, null=True, verbose_name='\u0410\u0434\u0440\u0435\u0441', blank=True),
        ),
        migrations.AlterField(
            model_name='ms',
            name='description',
            field=models.TextField(null=True, verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435', blank=True),
        ),
        migrations.AlterField(
            model_name='ms',
            name='fax',
            field=models.CharField(max_length=1000, null=True, verbose_name='\u0424\u0430\u043a\u0441', blank=True),
        ),
        migrations.AlterField(
            model_name='ms',
            name='mail',
            field=models.EmailField(max_length=254, null=True, verbose_name='\u042d\u043b\u0435\u043a\u0442\u0440\u043e\u043d\u043d\u0430\u044f \u043f\u043e\u0447\u0442\u0430', blank=True),
        ),
        migrations.AlterField(
            model_name='ms',
            name='name',
            field=models.CharField(unique=True, max_length=1000, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435'),
        ),
        migrations.AlterField(
            model_name='ms',
            name='org',
            field=models.ForeignKey(verbose_name='\u041e\u0440\u0433\u0430\u043d\u0438\u0437\u0430\u0446\u0438\u044f', to='core.Orgs'),
        ),
        migrations.AlterField(
            model_name='ms',
            name='phone',
            field=models.CharField(max_length=1000, null=True, verbose_name='\u0422\u0435\u043b\u0435\u0444\u043e\u043d', blank=True),
        ),
        migrations.AlterField(
            model_name='ms',
            name='site',
            field=models.CharField(max_length=1000, null=True, verbose_name='\u0421\u0430\u0439\u0442', blank=True),
        ),
        migrations.AlterField(
            model_name='ms',
            name='target_group',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='ms',
            name='type',
            field=models.ForeignKey(verbose_name='\u0422\u0438\u043f \u043f\u043e\u0434\u0440\u0430\u0437\u0434\u0435\u043b\u0435\u043d\u0438\u044f', to='core.SocialServiceType', null=True),
        ),
        migrations.AlterField(
            model_name='rehabprogram',
            name='file',
            field=models.FileField(upload_to=b'', null=True, verbose_name='\u0424\u0430\u0439\u043b', blank=True),
        ),
        migrations.AlterField(
            model_name='rehabprogram',
            name='name',
            field=models.CharField(max_length=1000, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435'),
        ),
        migrations.AlterField(
            model_name='rehabprogram',
            name='org',
            field=models.ForeignKey(verbose_name='\u041e\u0440\u0433\u0430\u043d\u0438\u0437\u0430\u0446\u0438\u044f', to='core.Orgs'),
        ),
        migrations.AlterField(
            model_name='religion',
            name='name',
            field=models.CharField(unique=True, max_length=1000, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435'),
        ),
        migrations.AlterField(
            model_name='routems',
            name='address',
            field=models.CharField(max_length=1000, null=True, verbose_name='\u0410\u0434\u0440\u0435\u0441', blank=True),
        ),
        migrations.AlterField(
            model_name='routems',
            name='description',
            field=models.TextField(null=True, verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435', blank=True),
        ),
        migrations.AlterField(
            model_name='routems',
            name='ms',
            field=models.ForeignKey(verbose_name='\u041c\u043e\u0431\u0438\u043b\u044c\u043d\u0430\u044f \u0441\u043b\u0443\u0436\u0431\u0430', to='core.MS'),
        ),
        migrations.AlterField(
            model_name='routems',
            name='time',
            field=models.CharField(unique=True, max_length=1000, verbose_name='\u0412\u0440\u0435\u043c\u044f'),
        ),
        migrations.AlterField(
            model_name='seat',
            name='created',
            field=models.DateField(auto_now_add=True, verbose_name='\u0414\u0430\u0442\u0430 \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f'),
        ),
        migrations.AlterField(
            model_name='seat',
            name='seats',
            field=models.IntegerField(null=True, verbose_name='\u041e\u0431\u0449\u0435\u0435 \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u043c\u0435\u0441\u0442', blank=True),
        ),
        migrations.AlterField(
            model_name='seat',
            name='seats_for_men',
            field=models.IntegerField(null=True, verbose_name='\u041c\u0435\u0441\u0442\u0430 \u0434\u043b\u044f \u043c\u0443\u0436\u0447\u0438\u043d', blank=True),
        ),
        migrations.AlterField(
            model_name='seat',
            name='seats_for_woman',
            field=models.IntegerField(null=True, verbose_name='\u041c\u0435\u0441\u0442\u0430 \u0434\u043b\u044f \u0436\u0435\u043d\u0449\u0438\u043d', blank=True),
        ),
        migrations.AlterField(
            model_name='seat',
            name='social_service',
            field=models.ForeignKey(verbose_name='\u041f\u043e\u0434\u0440\u0430\u0437\u0434\u0435\u043b\u0435\u043d\u0438\u0435', to='core.SocialService'),
        ),
        migrations.AlterField(
            model_name='socialservice',
            name='address',
            field=models.CharField(max_length=1000, null=True, verbose_name='\u0410\u0434\u0440\u0435\u0441', blank=True),
        ),
        migrations.AlterField(
            model_name='socialservice',
            name='description',
            field=models.TextField(null=True, verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435', blank=True),
        ),
        migrations.AlterField(
            model_name='socialservice',
            name='fax',
            field=models.CharField(max_length=1000, null=True, verbose_name='\u0424\u0430\u043a\u0441', blank=True),
        ),
        migrations.AlterField(
            model_name='socialservice',
            name='mail',
            field=models.EmailField(max_length=254, null=True, verbose_name='\u042d\u043b\u0435\u043a\u0442\u0440\u043e\u043d\u043d\u0430\u044f \u043f\u043e\u0447\u0442\u0430', blank=True),
        ),
        migrations.AlterField(
            model_name='socialservice',
            name='name',
            field=models.CharField(unique=True, max_length=1000, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435'),
        ),
        migrations.AlterField(
            model_name='socialservice',
            name='org',
            field=models.ForeignKey(verbose_name='\u041e\u0440\u0433\u0430\u043d\u0438\u0437\u0430\u0446\u0438\u044f', to='core.Orgs'),
        ),
        migrations.AlterField(
            model_name='socialservice',
            name='phone',
            field=models.CharField(max_length=1000, null=True, verbose_name='\u0422\u0435\u043b\u0435\u0444\u043e\u043d', blank=True),
        ),
        migrations.AlterField(
            model_name='socialservice',
            name='site',
            field=models.CharField(max_length=1000, null=True, verbose_name='\u0421\u0430\u0439\u0442', blank=True),
        ),
        migrations.AlterField(
            model_name='socialservice',
            name='target_group',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='socialservice',
            name='type',
            field=models.ForeignKey(verbose_name='\u0422\u0438\u043f \u043f\u043e\u0434\u0440\u0430\u0437\u0434\u0435\u043b\u0435\u043d\u0438\u044f', to='core.SocialServiceType', null=True),
        ),
        migrations.AlterField(
            model_name='socialserviceitem',
            name='name',
            field=models.CharField(max_length=1000, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435'),
        ),
        migrations.AlterField(
            model_name='socialservicetargetgroup',
            name='name',
            field=models.CharField(unique=True, max_length=1000, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435'),
        ),
        migrations.AlterField(
            model_name='socialservicetype',
            name='color',
            field=colorful.fields.RGBColorField(default=b'0095B6', verbose_name='\u0426\u0432\u0435\u0442 \u043c\u0435\u0442\u043a\u0438'),
        ),
        migrations.AlterField(
            model_name='socialservicetype',
            name='description',
            field=models.TextField(null=True, verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435', blank=True),
        ),
        migrations.AlterField(
            model_name='socialservicetype',
            name='name',
            field=models.CharField(unique=True, max_length=1000, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435'),
        ),
        migrations.AlterField(
            model_name='specialisttype',
            name='name',
            field=models.CharField(max_length=1000, verbose_name='\u0418\u043c\u044f \u0441\u043f\u0435\u0446\u0438\u0430\u043b\u0438\u0441\u0442\u0430'),
        ),
        migrations.AlterField(
            model_name='typeorgs',
            name='name',
            field=models.CharField(unique=True, max_length=1000, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435'),
        ),
    ]
