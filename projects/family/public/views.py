# -*- coding: utf-8 -*-

from django.views.generic import *
from public import models
from core.models import TypeOrgs

class TemplateMixin(object):
    title = u'ГБУ "Семья"'
    description = None
    keywords = None

    def get_title(self):
        return self.title

    def get_context_data(self, **kwargs):
        context = super(TemplateMixin, self).get_context_data(**kwargs)
        context.update({'title': self.get_title(),
                        'description': self.description,
                        'keywords':self.keywords,
                        'public': True,
                        })
        return context


# Template Views

class IndexView(TemplateMixin, TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        if models.FlatPage.objects.filter(type=models.PAGE_INDEX).exists():
            context.update({
                'object': models.FlatPage.objects.get(type=models.PAGE_INDEX),
                'public': True,
            })
        return context


class HomeView(TemplateMixin, TemplateView):
    template_name = 'home.html'
    title = u'ГИМЦ “Семья”'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        if models.FlatPage.objects.filter(type=models.PAGE_HOME).exists():
            context.update({
                'object': models.FlatPage.objects.get(type=models.PAGE_HOME),
                'personal':models.Personal.objects.all()
            })
        return context


class MapView(TemplateMixin, TemplateView):
    template_name = 'map.html'
    title = u'Система комплексной реабилитации наркозависимых в Санкт-Петербурге'

    def get_context_data(self, **kwargs):
        context = super(MapView, self).get_context_data(**kwargs)
        typeorgs = TypeOrgs.objects.exclude(orgs__isnull=True)
        context['typeorgs']=typeorgs
        if models.FlatPage.objects.filter(type=models.PAGE_MAP).exists():
            context.update({
                'object': models.FlatPage.objects.get(type=models.PAGE_MAP),
            })
        return context