# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from core.models import *

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0091_auto_20151130_1747'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='certificateforpatientsstep',
            name='uuid',
        ),
        migrations.AddField(
            model_name='consultation',
            name='id_in_organization',
            field=models.PositiveIntegerField(null=True, verbose_name=b'\xd0\x9f\xd0\xbe\xd1\x80\xd1\x8f\xd0\xb4\xd0\xba\xd0\xbe\xd0\xb2\xd1\x8b\xd0\xb9 \xd0\xbd\xd0\xbe\xd0\xbc\xd0\xb5\xd1\x80 \xd0\xba\xd0\xbe\xd0\xbd\xd1\x81\xd1\x83\xd0\xbb\xd1\x8c\xd1\x82\xd0\xb0\xd1\x86\xd0\xb8\xd0\xb8 \xd0\xb2 \xd0\xbe\xd1\x80\xd0\xb3\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb7\xd0\xb0\xd1\x86\xd0\xb8\xd0\xb8', blank=True),
        ),
        migrations.AddField(
            model_name='orgs',
            name='is_certificate_for_patients',
            field=models.BooleanField(default=False, verbose_name=b'\xd0\x9e\xd0\xb1\xd1\x81\xd0\xbb\xd1\x83\xd0\xb6\xd0\xb8\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5 \xd0\xbf\xd0\xbe \xd1\x81\xd0\xb5\xd1\x80\xd1\x82\xd0\xb8\xd1\x84\xd0\xb8\xd0\xba\xd0\xb0\xd1\x82\xd0\xb0\xd0\xbc'),
        ),
        migrations.AddField(
            model_name='consultation',
            name='from_social_service',
            field=models.ForeignKey(verbose_name=b'\xd0\x9d\xd0\xb0\xd0\xbf\xd1\x80\xd0\xb0\xd0\xb2\xd0\xbb\xd0\xb5\xd0\xbd \xd0\xb8\xd0\xb7', blank=True, to='core.SocialService', null=True),
        ),
        migrations.AddField(
            model_name='consultation',
            name='from_social_service_text',
            field=models.CharField(max_length=1000, null=True, verbose_name=b'\xd0\x9d\xd0\xb0\xd0\xbf\xd1\x80\xd0\xb0\xd0\xb2\xd0\xbb\xd0\xb5\xd0\xbd \xd0\xb8\xd0\xb7', blank=True),
        ),
        migrations.RemoveField(
            model_name='consultation',
            name='sent_to',
        ),
        migrations.AddField(
            model_name='consultation',
            name='sent_to',
            field=models.ManyToManyField(related_name='core_consultation_related', verbose_name=b'\xd0\x9d\xd0\xb0\xd0\xbf\xd1\x80\xd0\xb0\xd0\xb2\xd0\xbb\xd0\xb5\xd0\xbd \xd0\xb2', to='core.SocialService', blank=True),
        ),
        migrations.RemoveField(
            model_name='consultation',
            name='recommended_specialist',
        ),
        migrations.AddField(
            model_name='consultation',
            name='specialist_1',
            field=models.BooleanField(default=False, verbose_name=b'\xd0\x9f\xd1\x81\xd0\xb8\xd1\x85\xd0\xbe\xd0\xbb\xd0\xbe\xd0\xb3\xd1\x83'),
        ),
        migrations.AddField(
            model_name='consultation',
            name='specialist_2',
            field=models.BooleanField(default=False, verbose_name=b'\xd0\xae\xd1\x80\xd0\xb8\xd1\x81\xd1\x82\xd1\x83'),
        ),
        migrations.AddField(
            model_name='consultation',
            name='specialist_3',
            field=models.BooleanField(default=False, verbose_name=b'\xd0\x92\xd1\x80\xd0\xb0\xd1\x87\xd1\x83-\xd0\xbd\xd0\xb0\xd1\x80\xd0\xba\xd0\xbe\xd0\xbb\xd0\xbe\xd0\xb3\xd1\x83'),
        ),
        migrations.AddField(
            model_name='consultation',
            name='specialist_4',
            field=models.BooleanField(default=False, verbose_name=b'\xd0\x9f\xd0\xb5\xd0\xb4\xd0\xb0\xd0\xb3\xd0\xbe\xd0\xb3\xd1\x83'),
        ),
        migrations.AddField(
            model_name='consultation',
            name='specialist_5',
            field=models.BooleanField(default=False, verbose_name=b'\xd0\x92\xd1\x80\xd0\xb0\xd1\x87\xd1\x83-\xd0\xb8\xd0\xbc\xd0\xbc\xd1\x83\xd0\xbd\xd0\xbe\xd0\xbb\xd0\xbe\xd0\xb3\xd1\x83'),
        ),
        migrations.AddField(
            model_name='consultation',
            name='specialist_6',
            field=models.BooleanField(default=False, verbose_name=b'\xd0\xa1\xd0\xbf\xd0\xb5\xd1\x86\xd0\xb8\xd0\xb0\xd0\xbb\xd0\xb8\xd1\x81\xd1\x82\xd1\x83 \xd0\xbf\xd0\xbe \xd1\x80\xd0\xb0\xd0\xb1\xd0\xbe\xd1\x82\xd0\xb5 \xd1\x81 \xd1\x81\xd0\xb5\xd0\xbc\xd1\x8c\xd0\xb5\xd0\xb9'),
        ),
        migrations.AddField(
            model_name='consultation',
            name='specialist_7',
            field=models.BooleanField(default=False, verbose_name=b'\xd0\x9f\xd1\x81\xd0\xb8\xd1\x85\xd0\xbe\xd1\x82\xd0\xb5\xd1\x80\xd0\xb0\xd0\xbf\xd0\xb5\xd0\xb2\xd1\x82\xd1\x83'),
        ),
        migrations.AddField(
            model_name='consultation',
            name='specialist_8',
            field=models.BooleanField(default=False, verbose_name=b'\xd0\xa1\xd0\xbf\xd0\xb5\xd1\x86\xd0\xb8\xd0\xb0\xd0\xbb\xd0\xb8\xd1\x81\xd1\x82\xd1\x83 \xd0\xbf\xd0\xbe \xd1\x81\xd0\xbe\xd1\x86\xd0\xb8\xd0\xb0\xd0\xbb\xd1\x8c\xd0\xbd\xd0\xbe\xd0\xb9 \xd1\x80\xd0\xb0\xd0\xb1\xd0\xbe\xd1\x82\xd0\xb5'),
        ),
        migrations.AddField(
            model_name='consultation',
            name='specialist_text',
            field=models.CharField(max_length=1000, null=True, verbose_name=b'\xd0\x94\xd1\x80\xd1\x83\xd0\xb3\xd0\xb8\xd0\xb5 \xd1\x81\xd0\xbf\xd0\xb5\xd1\x86\xd0\xb8\xd0\xb0\xd0\xbb\xd0\xb8\xd1\x81\xd1\x82\xd1\x8b', blank=True),
        ),
    ]
