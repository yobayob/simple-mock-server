# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0090_auto_20151118_1502'),
    ]

    operations = [
        migrations.CreateModel(
            name='CertificateForPatients',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_start', models.DateField(null=True, verbose_name='\u0414\u0430\u0442\u0430 \u043d\u0430\u0447\u0430\u043b\u0430')),
                ('date_end', models.DateField(null=True, verbose_name='\u0414\u0430\u0442\u0430 \u0438\u0441\u0442\u0435\u0447\u0435\u043d\u0438\u044f')),
                ('uuid', models.UUIDField(default=uuid.uuid4, verbose_name='UUID', editable=False)),
                ('created', models.DateField(auto_now_add=True, null=True)),
                ('changed', models.DateField(auto_now=True, null=True)),
            ],
            options={
                'verbose_name': '\u0421\u0435\u0440\u0442\u0438\u0444\u0438\u043a\u0430\u0442 \u043d\u0430 \u043e\u043a\u0430\u0437\u0430\u043d\u0438\u0435 \u0443\u0441\u043b\u0443\u0433',
                'verbose_name_plural': 'C\u0435\u0440\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u044b \u043d\u0430 \u043e\u043a\u0430\u0437\u0430\u043d\u0438\u0435 \u0443\u0441\u043b\u0443\u0433',
            },
        ),
        migrations.CreateModel(
            name='CertificateForPatientsStep',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.IntegerField(default=None, null=True, verbose_name='\u0421\u0442\u0430\u0442\u0443\u0441', choices=[(None, '\u0412\u044b\u0434\u0430\u043d'), (1, '\u041f\u043e\u0433\u0430\u0448\u0435\u043d')])),
                ('step', models.IntegerField(default=1, choices=[(None, '\u041d\u0435\u0442 \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u0438'), (1, '\u041e\u0442\u043c\u0435\u0442\u043a\u0430 \u043e \u043d\u0430\u0447\u0430\u043b\u0430 \u043f\u0440\u043e\u0445\u043e\u0436\u0434\u0435\u043d\u0438\u044f \u043a\u0443\u0440\u0441\u0430 \u0441\u043e\u0446\u0438\u0430\u043b\u044c\u043d\u043e\u0439 \u0440\u0435\u0430\u0431\u0438\u043b\u0438\u0442\u0430\u0446\u0438\u0438'), (2, '\u041e\u0442\u043c\u0435\u0442\u043a\u0430 \u043e \u0437\u0430\u0432\u0435\u0440\u0448\u0435\u043d\u0438\u0438 \u043a\u0443\u0440\u0441\u0430 \u0441\u043e\u0446\u0438\u0430\u043b\u044c\u043d\u043e\u0439 \u0440\u0435\u0430\u0431\u0438\u043b\u0438\u0442\u0430\u0446\u0438\u0438'), (3, '\u041e\u0442\u043c\u0435\u0442\u043a\u0430 \u043e \u043d\u0430\u0447\u0430\u043b\u0435 \u043f\u043e\u0441\u0442\u0440\u0435\u0430\u0431\u0438\u043b\u0438\u0442\u0430\u0446\u0438\u043e\u043d\u043d\u043e\u0433\u043e \u043f\u0435\u0440\u0438\u043e\u0434\u0430'), (4, '\u041e\u0442\u043c\u0435\u0442\u043a\u0430 \u043e \u0437\u0430\u0432\u0435\u0440\u0448\u0435\u043d\u0438\u0438 \u043f\u043e\u0441\u0442\u0440\u0435\u0430\u0431\u0438\u043b\u0438\u0442\u0430\u0446\u0438\u043e\u043d\u043d\u043e\u0433\u043e \u043f\u0435\u0440\u0438\u043e\u0434\u0430')])),
                ('date_start', models.DateField(null=True, verbose_name='\u0414\u0430\u0442\u0430 \u043d\u0430\u0447\u0430\u043b\u0430')),
                ('date_end', models.DateField(null=True, verbose_name='\u0414\u0430\u0442\u0430 \u0438\u0441\u0442\u0435\u0447\u0435\u043d\u0438\u044f')),
                ('uuid', models.UUIDField(default=uuid.uuid4, verbose_name='UUID', editable=False)),
                ('created', models.DateField(auto_now_add=True, null=True)),
                ('changed', models.DateField(auto_now=True, null=True)),
                ('certificate', models.ForeignKey(verbose_name='\u0421\u0435\u0440\u0442\u0438\u0444\u0438\u043a\u0430\u0442', to='core.CertificateForPatients')),
            ],
            options={
                'verbose_name': '\u041a\u0443\u043f\u043e\u043d \u0441\u0435\u0440\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u0430',
                'verbose_name_plural': '\u041a\u0443\u043f\u043e\u043d \u0441\u0435\u0440\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u0430',
            },
        ),
        migrations.CreateModel(
            name='Consultation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('primary_treatment', models.BooleanField(default=False, verbose_name=b'\xd0\x9f\xd0\xb5\xd1\x80\xd0\xb2\xd0\xb8\xd1\x87\xd0\xbd\xd0\xbe\xd0\xb5 \xd0\xbe\xd0\xb1\xd1\x80\xd0\xb0\xd1\x89\xd0\xb5\xd0\xbd\xd0\xb8\xd0\xb5 \xd1\x81 \xd0\xbf\xd1\x80\xd0\xbe\xd0\xb1\xd0\xbb\xd0\xb5\xd0\xbc\xd0\xbe\xd0\xb9')),
                ('primary_treatment_org', models.BooleanField(default=False, verbose_name=b'\xd0\x9f\xd0\xb5\xd1\x80\xd0\xb2\xd0\xb8\xd1\x87\xd0\xbd\xd0\xbe\xd0\xb5 \xd0\xbe\xd0\xb1\xd1\x80\xd0\xb0\xd1\x89\xd0\xb5\xd0\xbd\xd0\xb8\xd0\xb5 \xd0\xb2 \xd0\xbe\xd1\x80\xd0\xb3\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb7\xd0\xb0\xd1\x86\xd0\xb8\xd1\x8e')),
                ('specialist', models.TextField(null=True, verbose_name=b'\xd0\xa1\xd0\xb2\xd0\xb5\xd0\xb4\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x8f \xd0\xbe \xd1\x81\xd0\xbf\xd0\xb5\xd1\x86\xd0\xb8\xd0\xb0\xd0\xbb\xd0\xb8\xd1\x81\xd1\x82\xd0\xb0\xd1\x85')),
                ('date', models.DateField(null=True, verbose_name='\u0414\u0430\u0442\u0430 \u043a\u043e\u043d\u0441\u0443\u043b\u044c\u0442\u0430\u0446\u0438\u0438')),
                ('status', models.IntegerField(default=None, null=True, verbose_name='\u0421\u0442\u0430\u0442\u0443\u0441', choices=[(None, '\u041d\u0435\u0442 \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u0438'), (1, '\u041e\u0431\u0440\u0430\u0442\u0438\u043b\u0441\u044f'), (2, '\u041e\u0431\u0440\u0430\u0442\u0438\u043b\u0441\u044f \u0432 \u0434\u0440\u0443\u0433\u0443\u044e \u043e\u0440\u0433\u0430\u043d\u0438\u0437\u0430\u0446\u0438\u044e'), (3, '\u041e\u0442\u043c\u0435\u043d\u0435\u043d\u043e')])),
                ('treatment', models.TextField(null=True, verbose_name='\u041a\u0440\u0430\u0442\u043a\u043e\u0435 \u043e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u0441\u043e\u0434\u0435\u0440\u0436\u0430\u043d\u0438\u044f \u043e\u0431\u0440\u0430\u0449\u0435\u043d\u0438\u044f', blank=True)),
                ('result_info', models.TextField(null=True, verbose_name='\u041a\u0440\u0430\u0442\u043a\u043e\u0435 \u043e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u0440\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442\u043e\u0432 \u043a\u043e\u043d\u0441\u0443\u043b\u044c\u0442\u0430\u0446\u0438\u0438', blank=True)),
                ('description', models.TextField(null=True, verbose_name='\u0414\u043e\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044c\u043d\u0430\u044f \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f', blank=True)),
                ('sent_to_text', models.CharField(max_length=1000, null=True, verbose_name=b'\xd0\x9d\xd0\xb0\xd0\xbf\xd1\x80\xd0\xb0\xd0\xb2\xd0\xbb\xd0\xb5\xd0\xbd \xd0\xb2', blank=True)),
                ('phone', models.CharField(max_length=1000, null=True, verbose_name='\u0422\u0435\u043b\u0435\u0444\u043e\u043d', blank=True)),
                ('email', models.CharField(max_length=1000, null=True, verbose_name='\u042d\u043b\u0435\u043a\u0442\u0440\u043e\u043d\u043d\u0430\u044f \u043f\u043e\u0447\u0442\u0430', blank=True)),
                ('additional_info_1', models.BooleanField(default=False, verbose_name=b'\xd0\x9e \xd0\xbd\xd0\xb0\xd0\xbb\xd0\xb8\xd1\x87\xd0\xb8\xd0\xb8 \xd0\xb2\xd0\xb0\xd0\xba\xd0\xb0\xd0\xbd\xd1\x81\xd0\xb8\xd0\xb9/\xd0\xbf\xd0\xbe\xd1\x80\xd1\x8f\xd0\xb4\xd0\xba\xd0\xb5 \xd0\xbe\xd0\xb1\xd1\x80\xd0\xb0\xd1\x89\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x8f \xd0\xb2 \xd1\x81\xd0\xbb\xd1\x83\xd0\xb6\xd0\xb1\xd1\x83 \xd0\xb7\xd0\xb0\xd0\xbd\xd1\x8f\xd1\x82\xd0\xbe\xd1\x81\xd1\x82\xd0\xb8')),
                ('additional_info_2', models.BooleanField(default=False, verbose_name=b'\xd0\x9e \xd0\xbf\xd0\xbe\xd1\x80\xd1\x8f\xd0\xb4\xd0\xba\xd0\xb5 \xd0\xbf\xd1\x80\xd0\xb5\xd0\xb4\xd0\xbe\xd1\x81\xd1\x82\xd0\xb0\xd0\xb2\xd0\xbb\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x8f \xd0\xbf\xd0\xbe\xd0\xbc\xd0\xbe\xd1\x89\xd0\xb8 \xd0\x92\xd0\x98\xd0\xa7-\xd0\xb8\xd0\xbd\xd1\x84\xd0\xb8\xd1\x86\xd0\xb8\xd1\x80\xd0\xbe\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xbd\xd1\x8b\xd0\xbc')),
                ('additional_info_3', models.BooleanField(default=False, verbose_name=b'\xd0\x9e \xd1\x80\xd0\xb5\xd0\xb6\xd0\xb8\xd0\xbc\xd0\xb5 \xd0\xb8 \xd0\xbf\xd0\xbe\xd1\x80\xd1\x8f\xd0\xb4\xd0\xba\xd0\xb5 \xd1\x80\xd0\xb0\xd0\xb1\xd0\xbe\xd1\x82\xd1\x8b \xd0\xb3\xd1\x80\xd1\x83\xd0\xbf\xd0\xbf \xd0\xb2\xd0\xb7\xd0\xb0\xd0\xb8\xd0\xbc\xd0\xbe\xd0\xbf\xd0\xbe\xd0\xbc\xd0\xbe\xd1\x89\xd0\xb8')),
                ('additional_info_4', models.BooleanField(default=False, verbose_name=b'\xd0\x9e \xd0\xbf\xd0\xbe\xd1\x80\xd1\x8f\xd0\xb4\xd0\xba\xd0\xb5 \xd0\xbf\xd0\xbe\xd0\xbb\xd1\x83\xd1\x87\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x8f \xd1\x83\xd1\x81\xd0\xbb\xd1\x83\xd0\xb3 \xd0\xbf\xd0\xbe \xd1\x81\xd0\xbe\xd1\x86\xd0\xb8\xd0\xb0\xd0\xbb\xd1\x8c\xd0\xbd\xd0\xbe\xd0\xb9 \xd1\x80\xd0\xb5\xd0\xb0\xd0\xb1\xd0\xb8\xd0\xbb\xd0\xb8\xd1\x82\xd0\xb0\xd1\x86\xd0\xb8\xd0\xb8 \xd0\xb8 \xd1\x80\xd0\xb5\xd1\x81\xd0\xbe\xd1\x86\xd0\xb8\xd0\xb0\xd0\xbb\xd0\xb8\xd0\xb7\xd0\xb0\xd1\x86\xd0\xb8\xd0\xb8')),
                ('additional_info_5', models.BooleanField(default=False, verbose_name=b'\xd0\x9e \xd0\xbf\xd0\xbe\xd1\x80\xd1\x8f\xd0\xb4\xd0\xba\xd0\xb5 \xd0\xbf\xd0\xbe\xd0\xbb\xd1\x83\xd1\x87\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x8f \xd1\x81\xd0\xbe\xd1\x86\xd0\xb8\xd0\xb0\xd0\xbb\xd1\x8c\xd0\xbd\xd1\x8b\xd1\x85 \xd1\x83\xd1\x81\xd0\xbb\xd1\x83\xd0\xb3')),
                ('additional_info_6', models.BooleanField(default=False, verbose_name=b'\xd0\x9e \xd0\xbf\xd0\xbe\xd1\x80\xd1\x8f\xd0\xb4\xd0\xba\xd0\xb5 \xd0\xbf\xd0\xbe\xd0\xbb\xd1\x83\xd1\x87\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x8f \xd0\xbc\xd0\xb5\xd0\xb4\xd0\xb8\xd1\x86\xd0\xb8\xd0\xbd\xd1\x81\xd0\xba\xd0\xbe\xd0\xb9 \xd0\xbf\xd0\xbe\xd0\xbc\xd0\xbe\xd1\x89\xd0\xb8')),
                ('additional_info_7', models.BooleanField(default=False, verbose_name=b'\xd0\x9e \xd1\x81\xd0\xbb\xd1\x83\xd0\xb6\xd0\xb1\xd0\xb0\xd1\x85 \xd0\xb7\xd0\xb0\xd0\xbd\xd1\x8f\xd1\x82\xd0\xbe\xd1\x81\xd1\x82\xd0\xb8 \xd0\xbd\xd0\xb0\xd1\x81\xd0\xb5\xd0\xbb\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x8f')),
                ('additional_info_8', models.BooleanField(default=False, verbose_name=b'\xd0\x9e \xd0\xa1\xd0\x9f\xd0\x98\xd0\x94-\xd1\x86\xd0\xb5\xd0\xbd\xd1\x82\xd1\x80\xd0\xb0\xd1\x85')),
                ('additional_info_9', models.BooleanField(default=False, verbose_name=b'\xd0\x9e \xd0\xb3\xd1\x80\xd1\x83\xd0\xbf\xd0\xbf\xd0\xb0\xd1\x85 \xd0\xb2\xd0\xb7\xd0\xb0\xd0\xb8\xd0\xbc\xd0\xbe\xd0\xbf\xd0\xbe\xd0\xbc\xd0\xbe\xd1\x89\xd0\xb8')),
                ('additional_info_10', models.BooleanField(default=False, verbose_name=b'\xd0\x9e \xd1\x80\xd0\xb5\xd0\xb0\xd0\xb1\xd0\xb8\xd0\xbb\xd0\xb8\xd1\x82\xd0\xb0\xd1\x86\xd0\xb8\xd0\xbe\xd0\xbd\xd0\xbd\xd1\x8b\xd1\x85 \xd1\x86\xd0\xb5\xd0\xbd\xd1\x82\xd1\x80\xd0\xb0\xd1\x85 \xd0\xb4\xd0\xbb\xd1\x8f \xd0\xbb\xd0\xb8\xd1\x86, \xd0\xbe\xd1\x82\xd0\xba\xd0\xb0\xd0\xb7\xd0\xb0\xd0\xb2\xd1\x88\xd0\xb8\xd1\x85\xd1\x81\xd1\x8f \xd0\xbe\xd1\x82 \xd0\xbd\xd0\xb5\xd0\xbc\xd0\xb5\xd0\xb4\xd0\xb8\xd1\x86\xd0\xb8\xd0\xbd\xd1\x81\xd0\xba\xd0\xbe\xd0\xb3\xd0\xbe \xd0\xbf\xd0\xbe\xd1\x82\xd1\x80\xd0\xb5\xd0\xb1\xd0\xbb\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x8f \xd0\xbd\xd0\xb0\xd1\x80\xd0\xba\xd0\xbe\xd1\x82\xd0\xb8\xd0\xba\xd0\xbe\xd0\xb2')),
                ('additional_info_11', models.BooleanField(default=False, verbose_name=b'\xd0\x9e \xd0\xb3\xd0\xbe\xd1\x81\xd1\x83\xd0\xb4\xd0\xb0\xd1\x80\xd1\x81\xd1\x82\xd0\xb2\xd0\xb5\xd0\xbd\xd0\xbd\xd1\x8b\xd1\x85 \xd1\x83\xd1\x87\xd1\x80\xd0\xb5\xd0\xb6\xd0\xb4\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x8f\xd1\x85-\xd0\xbf\xd0\xbe\xd1\x81\xd1\x82\xd0\xb0\xd0\xb2\xd1\x89\xd0\xb8\xd0\xba\xd0\xb0\xd1\x85 \xd1\x81\xd0\xbe\xd1\x86\xd0\xb8\xd0\xb0\xd0\xbb\xd1\x8c\xd0\xbd\xd1\x8b\xd1\x85 \xd1\x83\xd1\x81\xd0\xbb\xd1\x83\xd0\xb3')),
                ('additional_info_12', models.BooleanField(default=False, verbose_name=b'\xd0\x9e \xd0\xbc\xd0\xb5\xd0\xb4\xd0\xb8\xd1\x86\xd0\xb8\xd0\xbd\xd1\x81\xd0\xba\xd0\xb8\xd1\x85 \xd1\x83\xd1\x87\xd1\x80\xd0\xb5\xd0\xb6\xd0\xb4\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x8f\xd1\x85 \xd0\xbd\xd0\xb0\xd1\x80\xd0\xba\xd0\xbe\xd0\xbb\xd0\xbe\xd0\xb3\xd0\xb8\xd1\x87\xd0\xb5\xd1\x81\xd0\xba\xd0\xbe\xd0\xb3\xd0\xbe \xd0\xbf\xd1\x80\xd0\xbe\xd1\x84\xd0\xb8\xd0\xbb\xd1\x8f')),
                ('created', models.DateField(auto_now_add=True, null=True)),
                ('changed', models.DateField(auto_now=True, null=True)),
                ('organization', models.ForeignKey(verbose_name='\u041e\u0440\u0433\u0430\u043d\u0438\u0437\u0430\u0446\u0438\u044f', to='core.Orgs')),
            ],
            options={
                'verbose_name': '\u041a\u043e\u043d\u0441\u0443\u043b\u044c\u0442\u0430\u0446\u0438\u044f',
                'verbose_name_plural': '\u041a\u043e\u043d\u0441\u0443\u043b\u044c\u0442\u0430\u0446\u0438\u0438',
            },
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=1000, verbose_name='\u0418\u043c\u044f')),
                ('middle_name', models.CharField(max_length=1000, null=True, verbose_name='\u041e\u0442\u0447\u0435\u0441\u0442\u0432\u043e', blank=True)),
                ('last_name', models.CharField(max_length=1000, null=True, verbose_name='\u0424\u0430\u043c\u0438\u043b\u0438\u044f', blank=True)),
                ('birth_date', models.DateField(null=True, verbose_name='\u0414\u0430\u0442\u0430 \u0440\u043e\u0436\u0434\u0435\u043d\u0438\u044f', blank=True)),
                ('sex', models.BooleanField(default=1, verbose_name='\u041f\u043e\u043b', choices=[(1, '\u041c\u0443\u0436\u0441\u043a\u043e\u0439'), (2, '\u0416\u0435\u043d\u0441\u043a\u0438\u0439')])),
                ('passport_series', models.IntegerField(null=True, verbose_name='\u0421\u0435\u0440\u0438\u044f \u043f\u0430\u0441\u043f\u043e\u0440\u0442\u0430', blank=True)),
                ('passport_number', models.IntegerField(null=True, verbose_name='\u041d\u043e\u043c\u0435\u0440 \u043f\u0430\u0441\u043f\u043e\u0440\u0442\u0430', blank=True)),
                ('setter_date', models.DateField(null=True, verbose_name='\u0414\u0430\u0442\u0430 \u0432\u044b\u0434\u0430\u0447\u0438 \u043f\u0430\u0441\u043f\u043e\u0440\u0442\u0430', blank=True)),
                ('setter_org', models.CharField(max_length=1000, null=True, verbose_name='\u041a\u0435\u043c \u0432\u044b\u0434\u0430\u043d \u043f\u0430\u0441\u043f\u043e\u0440\u0442', blank=True)),
            ],
            options={
                'verbose_name': '\u041f\u0430\u0446\u0438\u0435\u043d\u0442',
                'verbose_name_plural': '\u041f\u0430\u0446\u0438\u0435\u043d\u0442\u044b',
            },
        ),
        migrations.AlterModelOptions(
            name='specialisttype',
            options={'verbose_name': '\u0421\u043f\u0435\u0446\u0438\u0430\u043b\u044c\u043d\u043e\u0441\u0442\u044c', 'verbose_name_plural': '\u0421\u043f\u0435\u0446\u0438\u0430\u043b\u044c\u043d\u043e\u0441\u0442\u0438'},
        ),
        migrations.AddField(
            model_name='consultation',
            name='patient',
            field=models.ForeignKey(verbose_name='\u041f\u0430\u0446\u0438\u0435\u043d\u0442', to='core.Patient'),
        ),
        migrations.AddField(
            model_name='consultation',
            name='recommended_specialist',
            field=models.ManyToManyField(to='core.SpecialistType', verbose_name=b'\xd0\xa0\xd0\xb5\xd0\xba\xd0\xbe\xd0\xbc\xd0\xb5\xd0\xbd\xd0\xb4\xd0\xbe\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xbd\xd1\x8b\xd0\xb5 \xd1\x81\xd0\xbf\xd0\xb5\xd1\x86\xd0\xb8\xd0\xb0\xd0\xbb\xd0\xb8\xd1\x81\xd1\x82\xd1\x8b', blank=True),
        ),
        migrations.AddField(
            model_name='consultation',
            name='sent_to',
            field=models.ForeignKey(verbose_name=b'\xd0\x9d\xd0\xb0\xd0\xbf\xd1\x80\xd0\xb0\xd0\xb2\xd0\xbb\xd0\xb5\xd0\xbd \xd0\xb2', blank=True, to='core.SocialService', null=True),
        ),
        migrations.AddField(
            model_name='certificateforpatients',
            name='patient',
            field=models.ForeignKey(verbose_name='\u041f\u0430\u0446\u0438\u0435\u043d\u0442', to='core.Patient'),
        ),
        migrations.AddField(
            model_name='certificateforpatients',
            name='social_service',
            field=models.ForeignKey(verbose_name='\u041c\u0435\u0441\u0442\u043e \u043d\u0430\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u044f', to='core.SocialService'),
        ),
    ]
