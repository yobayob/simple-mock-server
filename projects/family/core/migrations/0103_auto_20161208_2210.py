# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
import core.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0102_auto_20161206_2251'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blank',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('reason_for_request', models.TextField(null=True, verbose_name='\u0426\u0435\u043b\u044c \u043e\u0431\u0440\u0430\u0449\u0435\u043d\u0438\u044f', blank=True)),
                ('phone', models.CharField(max_length=1000, verbose_name='\u0422\u0435\u043b\u0435\u0444\u043e\u043d')),
                ('citizenship', models.CharField(max_length=1000, verbose_name='\u0413\u0440\u0430\u0436\u0434\u0430\u043d\u0441\u0442\u0432\u043e')),
                ('category_of_client', models.CharField(max_length=1000, verbose_name='\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f \u0437\u0430\u044f\u0432\u0438\u0442\u0435\u043b\u044f')),
                ('education', models.PositiveIntegerField(verbose_name='\u041e\u0431\u0440\u0430\u0437\u043e\u0432\u0430\u043d\u0438\u0435', choices=[(0, '\u0421\u0440\u0435\u0434\u043d\u0435\u0435'), (1, '\u0412\u044b\u0441\u0448\u0435\u0435'), (2, '\u041d\u0435\u0437\u0430\u043a\u043e\u043d\u0447\u0435\u043d\u043d\u043e\u0435 \u0432\u044b\u0441\u0448\u0435\u0435')])),
                ('position', models.CharField(max_length=1000, verbose_name='\u041e\u0441\u043d\u043e\u0432\u043d\u0430\u044f \u043f\u0440\u043e\u0444\u0435\u0441\u0441\u0438\u044f')),
                ('job', models.PositiveIntegerField(verbose_name='\u041c\u0435\u0441\u0442\u043e \u0440\u0430\u0431\u043e\u0442\u044b', choices=[(0, '\u0420\u0430\u0431\u043e\u0442\u0430\u044e\u0449\u0438\u0439'), (1, '\u041d\u0435 \u0440\u0430\u0431\u043e\u0442\u0430\u044e\u0449\u0438\u0439'), (2, '\u0417\u0430\u0440\u0435\u0433\u0438\u0441\u0442\u0440\u0438\u0440\u043e\u0432\u0430\u043d \u043a\u0430\u043a \u0431\u0435\u0437\u0440\u0430\u0431\u043e\u0442\u043d\u044b\u0439')])),
                ('sources_of_income', models.CharField(max_length=1000, verbose_name='\u0418\u0441\u0442\u043e\u0447\u043d\u0438\u043a \u0434\u043e\u0445\u043e\u0434\u0430')),
                ('per_capita_income', models.CharField(max_length=1000, verbose_name='\u0421\u0440\u0435\u0434\u043d\u0435\u0434\u0443\u0448\u0435\u0432\u043e\u0439 \u0434\u043e\u0445\u043e\u0434')),
                ('nark', models.BooleanField(default=False, verbose_name='\u041d\u0430\u043b\u0438\u0447\u0438\u0435 \u043e\u0444\u0438\u0446\u0438\u0430\u043b\u044c\u043d\u043e\u0433\u043e \u0434\u043e\u043a\u0443\u043c\u0435\u043d\u0442\u0430, \u043f\u043e\u0434\u0442\u0432\u0435\u0440\u0436\u0434\u0430\u044e\u0449\u0435\u0433\u043e \u0434\u0438\u0430\u0433\u043d\u043e\u0437 \xab\u041d\u0430\u0440\u043a\u043e\u043c\u0430\u043d\u0438\u044f\xbb')),
                ('file', models.FileField(upload_to=core.models.get_file_path, null=True, verbose_name='\u0420\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442\u044b \u043e\u043f\u0440\u043e\u0441\u0430 \u043f\u043e\u043b\u0443\u0447\u0430\u0442\u0435\u043b\u044f \u0441\u043e\u0446\u0438\u0430\u043b\u044c\u043d\u044b\u0445 \u0443\u0441\u043b\u0443\u0433 \u043f\u043e \u043c\u0435\u0442\u043e\u0434\u0438\u043a\u0435 \xab\u0418\u043d\u0434\u0435\u043a\u0441 \u0442\u044f\u0436\u0435\u0441\u0442\u0438 \u0437\u0430\u0432\u0438\u0441\u0438\u043c\u043e\u0441\u0442\u0438\xbb (\u0444\u0430\u0439\u043b)', blank=True)),
                ('comment', models.TextField(null=True, verbose_name='\u041a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0439', blank=True)),
                ('created', models.DateField(auto_now_add=True, verbose_name='\u0421\u043e\u0437\u0434\u0430\u043d\u043e', null=True)),
                ('changed', models.DateField(auto_now=True, verbose_name='\u0418\u0437\u043c\u0435\u043d\u0435\u043d\u043e', null=True)),
                ('organization', models.ForeignKey(related_name='blanks', verbose_name='\u041e\u0440\u0433\u0430\u043d\u0438\u0437\u0430\u0446\u0438\u044f', to='core.Orgs')),
            ],
            options={
                'verbose_name': '\u0423\u0447\u0435\u0442\u043d\u0430\u044f \u043a\u0430\u0440\u0442\u043e\u0447\u043a\u0430',
                'verbose_name_plural': '\u0423\u0447\u0435\u0442\u043d\u044b\u0435 \u043a\u0430\u0440\u0442\u043e\u0447\u043a\u0438',
            },
        ),
        migrations.CreateModel(
            name='BlankService',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField(default=datetime.date(2016, 12, 8), verbose_name='\u0414\u0430\u0442\u0430 \u0443\u0441\u043b\u0443\u0433\u0438')),
                ('place', models.CharField(max_length=1000, verbose_name='\u041c\u0435\u0441\u0442\u043e \u043f\u0440\u043e\u0432\u0435\u0434\u0435\u043d\u0438\u044f \u0443\u0441\u043b\u0443\u0433\u0438')),
                ('file', models.FileField(upload_to=core.models.get_file_path, null=True, verbose_name='\u0420\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442\u044b \u0430\u043d\u043a\u0435\u0442\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u044f', blank=True)),
                ('cancelled_date', models.DateField(null=True, verbose_name='\u0414\u0430\u0442\u0430 \u043e\u0442\u043c\u0435\u043d\u044b \u0443\u0441\u043b\u0443\u0433\u0438', blank=True)),
                ('cancelled_reason', models.CharField(max_length=1000, null=True, verbose_name='\u041f\u0440\u0438\u0447\u0438\u043d\u0430 \u043e\u0442\u043c\u0435\u043d\u044b', blank=True)),
                ('created', models.DateField(auto_now_add=True, verbose_name='\u0421\u043e\u0437\u0434\u0430\u043d\u043e')),
                ('changed', models.DateField(auto_now=True, verbose_name='\u0418\u0437\u043c\u0435\u043d\u0435\u043d\u043e', null=True)),
                ('blank', models.ForeignKey(related_name='blank_services', verbose_name='\u0423\u0447\u0435\u0442\u043d\u0430\u044f \u043a\u0430\u0440\u0442\u043e\u0447\u043a\u0430 \u043f\u0430\u0446\u0438\u0435\u043d\u0442\u0430', to='core.Blank')),
            ],
            options={
                'verbose_name': '\u0424\u0430\u043a\u0442 \u043f\u043e\u043b\u0443\u0447\u0435\u043d\u0438\u044f \u0441\u043e\u0446\u0438\u0430\u043b\u044c\u043d\u044b\u0445 \u0443\u0441\u043b\u0443\u0433',
                'verbose_name_plural': '\u0421\u043e\u0446\u0438\u0430\u043b\u044c\u043d\u044b\u0435 \u0443\u0441\u043b\u0443\u0433\u0438',
            },
        ),
        migrations.CreateModel(
            name='BlankServiceItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=1000, verbose_name='\u041d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435 \u0443\u0441\u043b\u0443\u0433\u0438')),
                ('description', models.TextField(null=True, verbose_name='\u0414\u043e\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044c\u043d\u0430\u044f \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f', blank=True)),
                ('form_of_provision', models.ForeignKey(verbose_name='\u0424\u043e\u0440\u043c\u0430 \u043e\u043a\u0430\u0437\u0430\u043d\u0438\u044f \u0443\u0441\u043b\u0443\u0433\u0438', to='core.FormProvisionService')),
                ('organization', models.ForeignKey(verbose_name='\u041e\u0440\u0433\u0430\u043d\u0438\u0437\u0430\u0446\u0438\u044f', to='core.Orgs')),
            ],
            options={
                'verbose_name': '\u0423\u0441\u043b\u0443\u0433\u0430, \u043e\u043a\u0430\u0437\u044b\u0432\u0430\u0435\u043c\u0430\u044f \u0441\u043f\u0435\u0446\u0438\u0430\u043b\u0438\u0441\u0442\u043e\u043c',
                'verbose_name_plural': '\u0423\u0441\u043b\u0443\u0433\u0438, \u043e\u043a\u0430\u0437\u044b\u0432\u0430\u0435\u043c\u044b\u0435 \u0441\u043f\u0435\u0446\u0438\u0430\u043b\u0438\u0441\u0442\u0430\u043c\u0438',
            },
        ),
        migrations.CreateModel(
            name='FamilyMember',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('full_name', models.CharField(max_length=1000, verbose_name='\u041f\u043e\u043b\u043d\u043e\u0435 \u0438\u043c\u044f')),
                ('birthdate', models.DateField(verbose_name='\u0414\u0430\u0442\u0430 \u0440\u043e\u0436\u0434\u0435\u043d\u0438\u044f')),
                ('capacity', models.BooleanField(default=False, verbose_name='\u0414\u0435\u0435\u0441\u043f\u043e\u0441\u043e\u0431\u043d\u043e\u0441\u0442\u044c')),
                ('earning_capacity', models.BooleanField(default=False, verbose_name='\u0422\u0440\u0443\u0434\u043e\u0441\u043f\u043e\u0441\u043e\u0431\u043d\u043e\u0441\u0442\u044c')),
                ('relation_degree', models.CharField(max_length=1000, verbose_name='\u0421\u0442\u0435\u043f\u0435\u043d\u044c \u0440\u043e\u0434\u0441\u0442\u0432\u0430')),
                ('income', models.CharField(max_length=1000, verbose_name='\u0414\u043e\u0445\u043e\u0434')),
                ('registration', models.BooleanField(default=False, verbose_name='\u041d\u0430\u043b\u0438\u0447\u0438\u0435 \u0440\u0435\u0433\u0438\u0441\u0442\u0440\u0430\u0446\u0438\u0438 \u043f\u043e \u0430\u0434\u0440\u0435\u0441\u0443 \u0437\u0430\u044f\u0432\u0438\u0442\u0435\u043b\u044f')),
                ('blank', models.ForeignKey(related_name='family_members', verbose_name='\u0423\u0447\u0435\u0442\u043d\u0430\u044f \u043a\u0430\u0440\u0442\u043e\u0447\u043a\u0430 \u043f\u0430\u0446\u0438\u0435\u043d\u0442\u0430', to='core.Blank')),
            ],
            options={
                'verbose_name': '\u0427\u043b\u0435\u043d \u0441\u0435\u043c\u044c\u0438',
                'verbose_name_plural': '\u0427\u043b\u0435\u043d\u044b \u0441\u0435\u043c\u044c\u0438',
            },
        ),
        migrations.AddField(
            model_name='passport',
            name='address',
            field=models.TextField(null=True, verbose_name='\u0410\u0434\u0440\u0435\u0441 \u0440\u0435\u0433\u0438\u0441\u0442\u0440\u0430\u0446\u0438\u0438', blank=True),
        ),
        migrations.AddField(
            model_name='passport',
            name='fact_address',
            field=models.TextField(null=True, verbose_name='\u0410\u0434\u0440\u0435\u0441 \u043f\u0440\u043e\u0436\u0438\u0432\u0430\u043d\u0438\u044f', blank=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(upload_to=core.models.get_file_path, null=True, verbose_name='\u0410\u0432\u0430\u0442\u0430\u0440', blank=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='time_work',
            field=models.TextField(default='10:00 - 18:00', null=True, verbose_name='\u0412\u0440\u0435\u043c\u044f \u0440\u0430\u0431\u043e\u0442\u044b', blank=True),
        ),
        migrations.AddField(
            model_name='blankservice',
            name='service',
            field=models.ForeignKey(verbose_name='\u0423\u0441\u043b\u0443\u0433\u0430', to='core.BlankServiceItem'),
        ),
        migrations.AddField(
            model_name='blankservice',
            name='user',
            field=models.ForeignKey(related_name='blank_services', verbose_name='\u0421\u043f\u0435\u0446\u0438\u0430\u043b\u0438\u0441\u0442', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='blank',
            name='patient',
            field=models.ForeignKey(verbose_name='\u041a\u043b\u0438\u0435\u043d\u0442', to='core.Passport'),
        ),
    ]
