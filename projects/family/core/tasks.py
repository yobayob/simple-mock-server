# -*- coding: utf-8 -*-

from celery import task
from django.core.mail import send_mail
from django.conf import settings


@task(name="send_mail")
def send_mail_task(head, text, mails):
    for mail in mails:
        send_mail(head, text, settings.DEFAULT_FROM_EMAIL,  [mail], fail_silently=False)


@task(name="debug")
def debug_celery():
    return 'CELERY WORK!'