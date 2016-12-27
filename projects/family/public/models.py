# -*- coding: utf-8 -*-

from django.db import models
from tinymce.models import HTMLField
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from django.utils.translation import ugettext_lazy as _

PAGE_INDEX = 1
PAGE_MAP = 2
PAGE_FORM = 3
PAGE_HOME = 4

TYPE_PAGES_CHOICES = (
    (PAGE_INDEX, _(u'Главная')),
    (PAGE_MAP, _(u'Карта')),
    (PAGE_FORM, _(u'Подача заявки')),
    (PAGE_HOME, _(u'Страница отдела')),
)


class FlatPage(models.Model):
    title = models.CharField(max_length=1000, verbose_name=u'title')
    text_1 = HTMLField(null=True, blank=True, verbose_name=u'Текст 1')
    text_2 = HTMLField(null=True, blank=True, verbose_name=u'Текст 2')
    text_3 = HTMLField(null=True, blank=True, verbose_name=u'Текст 3')
    type = models.PositiveIntegerField(choices=TYPE_PAGES_CHOICES, verbose_name=u'Тип страницы')

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = u'Статичная страница'
        verbose_name_plural = u'Статичные страницы'


POSITION_CHOICES = (
    (1, _(u'Начальник отдела')),
    (2, _(u'Методист')),
    (3, _(u'Программист'))
)


class Personal(models.Model):
    name = models.CharField(max_length=1000, verbose_name=u'ФИО')
    position = models.PositiveIntegerField(choices=POSITION_CHOICES, verbose_name=u'Должность')
    phone = models.CharField(max_length=1000, default='8 (812) 417-31-51', verbose_name=u'Телефон')
    mail = models.EmailField(default='depeduspb@gmail.com', verbose_name=u'Почта')

    thumbnail = models.ImageField(null=True, blank=True, upload_to='personal/', verbose_name=u"Фото (желательно 200x200)")
    thumbnail_md = ImageSpecField( source='thumbnail',
                                   processors=[ResizeToFill(200, 300)],
                                   format='JPEG',
                                   options={'quality': 90})

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['position']
        verbose_name = u'Персонал'
        verbose_name_plural = u'Персонал'
