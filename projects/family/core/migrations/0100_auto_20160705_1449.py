# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0099_auto_20160331_1153'),
    ]

    operations = [
        migrations.CreateModel(
            name='Passport',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=1000, verbose_name='\u0418\u043c\u044f')),
                ('middle_name', models.CharField(max_length=1000, verbose_name='\u041e\u0442\u0447\u0435\u0441\u0442\u0432\u043e')),
                ('last_name', models.CharField(max_length=1000, verbose_name='\u0424\u0430\u043c\u0438\u043b\u0438\u044f')),
                ('birth_date', models.DateField(verbose_name='\u0414\u0430\u0442\u0430 \u0440\u043e\u0436\u0434\u0435\u043d\u0438\u044f')),
                ('sex', models.PositiveIntegerField(default=1, verbose_name='\u041f\u043e\u043b', choices=[(1, '\u041c\u0443\u0436\u0441\u043a\u043e\u0439'), (0, '\u0416\u0435\u043d\u0441\u043a\u0438\u0439')])),
                ('passport_series', models.IntegerField(verbose_name='\u0421\u0435\u0440\u0438\u044f \u043f\u0430\u0441\u043f\u043e\u0440\u0442\u0430')),
                ('passport_number', models.IntegerField(verbose_name='\u041d\u043e\u043c\u0435\u0440 \u043f\u0430\u0441\u043f\u043e\u0440\u0442\u0430')),
                ('setter_date', models.DateField(verbose_name='\u0414\u0430\u0442\u0430 \u0432\u044b\u0434\u0430\u0447\u0438 \u043f\u0430\u0441\u043f\u043e\u0440\u0442\u0430')),
                ('setter_org', models.CharField(max_length=1000, verbose_name='\u041a\u0435\u043c \u0432\u044b\u0434\u0430\u043d \u043f\u0430\u0441\u043f\u043e\u0440\u0442')),
            ],
            options={
                'verbose_name': '\u041a\u043b\u0438\u0435\u043d\u0442',
                'verbose_name_plural': '\u041a\u043b\u0438\u0435\u043d\u0442\u044b',
            },
        ),
        migrations.RenameField(
            model_name='patient',
            old_name='first_name',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='birth_date',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='middle_name',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='passport_number',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='passport_series',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='setter_date',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='setter_org',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='sex',
        ),
        migrations.AddField(
            model_name='certificateforpatients',
            name='status',
            field=models.IntegerField(default=10, verbose_name='\u0421\u0442\u0430\u0442\u0443\u0441', choices=[(10, '\u0417\u0430\u043f\u0440\u043e\u0448\u0435\u043d'), (20, '\u041e\u0434\u043e\u0431\u0440\u0435\u043d'), (30, '\u041e\u0442\u043a\u043b\u043e\u043d\u0435\u043d'), (40, '\u0412\u044b\u043f\u043e\u043b\u043d\u0435\u043d')]),
        ),
        migrations.AddField(
            model_name='orgs',
            name='is_query_certificate_for_patients',
            field=models.BooleanField(default=False, verbose_name='\u041f\u043e\u0434\u0430\u0447\u0430 \u0437\u0430\u044f\u0432\u043e\u043a \u043d\u0430 \u0441\u0435\u0440\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u044b'),
        ),
        migrations.AlterField(
            model_name='certificateforpatients',
            name='patient',
            field=models.ForeignKey(verbose_name='\u041a\u043b\u0438\u0435\u043d\u0442', to='core.Passport'),
        ),
        migrations.AlterField(
            model_name='consultation',
            name='additional_info_1',
            field=models.BooleanField(default=False, verbose_name='\u041e \u043d\u0430\u043b\u0438\u0447\u0438\u0438 \u0432\u0430\u043a\u0430\u043d\u0441\u0438\u0439/\u043f\u043e\u0440\u044f\u0434\u043a\u0435 \u043e\u0431\u0440\u0430\u0449\u0435\u043d\u0438\u044f \u0432 \u0441\u043b\u0443\u0436\u0431\u0443 \u0437\u0430\u043d\u044f\u0442\u043e\u0441\u0442\u0438'),
        ),
        migrations.AlterField(
            model_name='consultation',
            name='additional_info_10',
            field=models.BooleanField(default=False, verbose_name='\u041e \u0440\u0435\u0430\u0431\u0438\u043b\u0438\u0442\u0430\u0446\u0438\u043e\u043d\u043d\u044b\u0445 \u0446\u0435\u043d\u0442\u0440\u0430\u0445 \u0434\u043b\u044f \u043b\u0438\u0446, \u043e\u0442\u043a\u0430\u0437\u0430\u0432\u0448\u0438\u0445\u0441\u044f \u043e\u0442 \u043d\u0435\u043c\u0435\u0434\u0438\u0446\u0438\u043d\u0441\u043a\u043e\u0433\u043e \u043f\u043e\u0442\u0440\u0435\u0431\u043b\u0435\u043d\u0438\u044f \u043d\u0430\u0440\u043a\u043e\u0442\u0438\u043a\u043e\u0432'),
        ),
        migrations.AlterField(
            model_name='consultation',
            name='additional_info_11',
            field=models.BooleanField(default=False, verbose_name='\u041e \u0433\u043e\u0441\u0443\u0434\u0430\u0440\u0441\u0442\u0432\u0435\u043d\u043d\u044b\u0445 \u0443\u0447\u0440\u0435\u0436\u0434\u0435\u043d\u0438\u044f\u0445-\u043f\u043e\u0441\u0442\u0430\u0432\u0449\u0438\u043a\u0430\u0445 \u0441\u043e\u0446\u0438\u0430\u043b\u044c\u043d\u044b\u0445 \u0443\u0441\u043b\u0443\u0433'),
        ),
        migrations.AlterField(
            model_name='consultation',
            name='additional_info_12',
            field=models.BooleanField(default=False, verbose_name='\u041e \u043c\u0435\u0434\u0438\u0446\u0438\u043d\u0441\u043a\u0438\u0445 \u0443\u0447\u0440\u0435\u0436\u0434\u0435\u043d\u0438\u044f\u0445 \u043d\u0430\u0440\u043a\u043e\u043b\u043e\u0433\u0438\u0447\u0435\u0441\u043a\u043e\u0433\u043e \u043f\u0440\u043e\u0444\u0438\u043b\u044f'),
        ),
        migrations.AlterField(
            model_name='consultation',
            name='additional_info_2',
            field=models.BooleanField(default=False, verbose_name='\u041e \u043f\u043e\u0440\u044f\u0434\u043a\u0435 \u043f\u0440\u0435\u0434\u043e\u0441\u0442\u0430\u0432\u043b\u0435\u043d\u0438\u044f \u043f\u043e\u043c\u043e\u0449\u0438 \u0412\u0418\u0427-\u0438\u043d\u0444\u0438\u0446\u0438\u0440\u043e\u0432\u0430\u043d\u043d\u044b\u043c'),
        ),
        migrations.AlterField(
            model_name='consultation',
            name='additional_info_3',
            field=models.BooleanField(default=False, verbose_name='\u041e \u0440\u0435\u0436\u0438\u043c\u0435 \u0438 \u043f\u043e\u0440\u044f\u0434\u043a\u0435 \u0440\u0430\u0431\u043e\u0442\u044b \u0433\u0440\u0443\u043f\u043f \u0432\u0437\u0430\u0438\u043c\u043e\u043f\u043e\u043c\u043e\u0449\u0438'),
        ),
        migrations.AlterField(
            model_name='consultation',
            name='additional_info_4',
            field=models.BooleanField(default=False, verbose_name='\u041e \u043f\u043e\u0440\u044f\u0434\u043a\u0435 \u043f\u043e\u043b\u0443\u0447\u0435\u043d\u0438\u044f \u0443\u0441\u043b\u0443\u0433 \u043f\u043e \u0441\u043e\u0446\u0438\u0430\u043b\u044c\u043d\u043e\u0439 \u0440\u0435\u0430\u0431\u0438\u043b\u0438\u0442\u0430\u0446\u0438\u0438 \u0438 \u0440\u0435\u0441\u043e\u0446\u0438\u0430\u043b\u0438\u0437\u0430\u0446\u0438\u0438'),
        ),
        migrations.AlterField(
            model_name='consultation',
            name='additional_info_5',
            field=models.BooleanField(default=False, verbose_name='\u041e \u043f\u043e\u0440\u044f\u0434\u043a\u0435 \u043f\u043e\u043b\u0443\u0447\u0435\u043d\u0438\u044f \u0441\u043e\u0446\u0438\u0430\u043b\u044c\u043d\u044b\u0445 \u0443\u0441\u043b\u0443\u0433'),
        ),
        migrations.AlterField(
            model_name='consultation',
            name='additional_info_6',
            field=models.BooleanField(default=False, verbose_name='\u041e \u043f\u043e\u0440\u044f\u0434\u043a\u0435 \u043f\u043e\u043b\u0443\u0447\u0435\u043d\u0438\u044f \u043c\u0435\u0434\u0438\u0446\u0438\u043d\u0441\u043a\u043e\u0439 \u043f\u043e\u043c\u043e\u0449\u0438'),
        ),
        migrations.AlterField(
            model_name='consultation',
            name='additional_info_7',
            field=models.BooleanField(default=False, verbose_name='\u041e \u0441\u043b\u0443\u0436\u0431\u0430\u0445 \u0437\u0430\u043d\u044f\u0442\u043e\u0441\u0442\u0438 \u043d\u0430\u0441\u0435\u043b\u0435\u043d\u0438\u044f'),
        ),
        migrations.AlterField(
            model_name='consultation',
            name='additional_info_8',
            field=models.BooleanField(default=False, verbose_name='\u041e \u0421\u041f\u0418\u0414-\u0446\u0435\u043d\u0442\u0440\u0430\u0445'),
        ),
        migrations.AlterField(
            model_name='consultation',
            name='additional_info_9',
            field=models.BooleanField(default=False, verbose_name='\u041e \u0433\u0440\u0443\u043f\u043f\u0430\u0445 \u0432\u0437\u0430\u0438\u043c\u043e\u043f\u043e\u043c\u043e\u0449\u0438'),
        ),
        migrations.AlterField(
            model_name='consultation',
            name='from_social_service',
            field=models.ForeignKey(verbose_name='\u041d\u0430\u043f\u0440\u0430\u0432\u043b\u0435\u043d \u0438\u0437', blank=True, to='core.SocialService', null=True),
        ),
        migrations.AlterField(
            model_name='consultation',
            name='from_social_service_text',
            field=models.CharField(max_length=1000, null=True, verbose_name='\u041d\u0430\u043f\u0440\u0430\u0432\u043b\u0435\u043d \u0438\u0437', blank=True),
        ),
        migrations.AlterField(
            model_name='consultation',
            name='id_in_organization',
            field=models.PositiveIntegerField(null=True, verbose_name='\u041f\u043e\u0440\u044f\u0434\u043a\u043e\u0432\u044b\u0439 \u043d\u043e\u043c\u0435\u0440 \u043a\u043e\u043d\u0441\u0443\u043b\u044c\u0442\u0430\u0446\u0438\u0438 \u0432 \u043e\u0440\u0433\u0430\u043d\u0438\u0437\u0430\u0446\u0438\u0438', blank=True),
        ),
        migrations.AlterField(
            model_name='consultation',
            name='primary_treatment',
            field=models.BooleanField(default=False, verbose_name='\u041f\u0435\u0440\u0432\u0438\u0447\u043d\u043e\u0435 \u043e\u0431\u0440\u0430\u0449\u0435\u043d\u0438\u0435 \u0441 \u043f\u0440\u043e\u0431\u043b\u0435\u043c\u043e\u0439'),
        ),
        migrations.AlterField(
            model_name='consultation',
            name='primary_treatment_org',
            field=models.BooleanField(default=False, verbose_name='\u041f\u0435\u0440\u0432\u0438\u0447\u043d\u043e\u0435 \u043e\u0431\u0440\u0430\u0449\u0435\u043d\u0438\u0435 \u0432 \u043e\u0440\u0433\u0430\u043d\u0438\u0437\u0430\u0446\u0438\u044e'),
        ),
        migrations.AlterField(
            model_name='consultation',
            name='sent_to_text',
            field=models.CharField(max_length=1000, null=True, verbose_name='\u041d\u0430\u043f\u0440\u0430\u0432\u043b\u0435\u043d \u0432', blank=True),
        ),
        migrations.AlterField(
            model_name='consultation',
            name='specialist',
            field=models.TextField(null=True, verbose_name='\u0421\u0432\u0435\u0434\u0435\u043d\u0438\u044f \u043e \u0441\u043f\u0435\u0446\u0438\u0430\u043b\u0438\u0441\u0442\u0430\u0445'),
        ),
        migrations.AlterField(
            model_name='consultation',
            name='specialist_1',
            field=models.BooleanField(default=False, verbose_name='\u041f\u0441\u0438\u0445\u043e\u043b\u043e\u0433\u0443'),
        ),
        migrations.AlterField(
            model_name='consultation',
            name='specialist_2',
            field=models.BooleanField(default=False, verbose_name='\u042e\u0440\u0438\u0441\u0442\u0443'),
        ),
        migrations.AlterField(
            model_name='consultation',
            name='specialist_3',
            field=models.BooleanField(default=False, verbose_name='\u0412\u0440\u0430\u0447\u0443-\u043d\u0430\u0440\u043a\u043e\u043b\u043e\u0433\u0443'),
        ),
        migrations.AlterField(
            model_name='consultation',
            name='specialist_4',
            field=models.BooleanField(default=False, verbose_name='\u041f\u0435\u0434\u0430\u0433\u043e\u0433\u0443'),
        ),
        migrations.AlterField(
            model_name='consultation',
            name='specialist_5',
            field=models.BooleanField(default=False, verbose_name='\u0412\u0440\u0430\u0447\u0443-\u0438\u043c\u043c\u0443\u043d\u043e\u043b\u043e\u0433\u0443'),
        ),
        migrations.AlterField(
            model_name='consultation',
            name='specialist_6',
            field=models.BooleanField(default=False, verbose_name='\u0421\u043f\u0435\u0446\u0438\u0430\u043b\u0438\u0441\u0442\u0443 \u043f\u043e \u0440\u0430\u0431\u043e\u0442\u0435 \u0441 \u0441\u0435\u043c\u044c\u0435\u0439'),
        ),
        migrations.AlterField(
            model_name='consultation',
            name='specialist_7',
            field=models.BooleanField(default=False, verbose_name='\u041f\u0441\u0438\u0445\u043e\u0442\u0435\u0440\u0430\u043f\u0435\u0432\u0442\u0443'),
        ),
        migrations.AlterField(
            model_name='consultation',
            name='specialist_8',
            field=models.BooleanField(default=False, verbose_name='\u0421\u043f\u0435\u0446\u0438\u0430\u043b\u0438\u0441\u0442\u0443 \u043f\u043e \u0441\u043e\u0446\u0438\u0430\u043b\u044c\u043d\u043e\u0439 \u0440\u0430\u0431\u043e\u0442\u0435'),
        ),
        migrations.AlterField(
            model_name='consultation',
            name='specialist_text',
            field=models.CharField(max_length=1000, null=True, verbose_name='\u0414\u0440\u0443\u0433\u0438\u0435 \u0441\u043f\u0435\u0446\u0438\u0430\u043b\u0438\u0441\u0442\u044b', blank=True),
        ),
        migrations.AlterField(
            model_name='direction',
            name='consultation',
            field=models.ForeignKey(verbose_name='\u041a\u043e\u043d\u0441\u0443\u043b\u044c\u0442\u0430\u0446\u0438\u044f', to='core.Consultation'),
        ),
        migrations.AlterField(
            model_name='direction',
            name='social_service',
            field=models.ForeignKey(verbose_name='\u041d\u0430\u043f\u0440\u0430\u0432\u043b\u0435\u043d \u0432', to='core.SocialService'),
        ),
        migrations.AlterField(
            model_name='orgs',
            name='is_certificate_for_patients',
            field=models.BooleanField(default=False, verbose_name='\u041e\u0431\u0441\u043b\u0443\u0436\u0438\u0432\u0430\u043d\u0438\u0435 \u043f\u043e \u0441\u0435\u0440\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u0430\u043c'),
        ),
        migrations.AddField(
            model_name='passport',
            name='patient',
            field=models.ForeignKey(verbose_name='\u041a\u043b\u0438\u0435\u043d\u0442 ID (\u0415\u0441\u043b\u0438 \u0435\u0441\u0442\u044c \u0432 \u0431\u0430\u0437\u0435)', blank=True, to='core.Patient', null=True),
        ),
    ]
