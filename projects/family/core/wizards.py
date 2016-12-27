# -*- coding: utf-8 -*-
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from core import models, forms
from formtools.wizard.views import SessionWizardView
from collections import OrderedDict

class ClientWizard(SessionWizardView):
    """
    Общий wizard для создания консультаций и сертификатов
    """
    file_storage = 'var/media/CACHE/'
    url_name = "wizard_step"

    def get_step_url(self, step):
        return reverse(self.url_name, kwargs={'step': step})

    def _get_client(self):
        """
        Получаем данные клиента (либо существующие, либо те которые надо добавить)
        """
        if self.get_cleaned_data_for_step(self.steps.first)['client_code']:
            client = self.get_cleaned_data_for_step(self.steps.first)['client_code']
        else:
            client = self.get_cleaned_data_for_step(self.steps.first)
        return client

    def get_context_data(self, form, **kwargs):
        context = super(ClientWizard, self).get_context_data(form=form, **kwargs)
        if not self.steps.current == self.steps.first:
            client = self._get_client()
            context.update({'client': client})
        context.update({'title': u'Заполнение анкеты'})
        return context

    def get_form_kwargs(self, step):
        kwargs = super(ClientWizard, self).get_form_kwargs()
        if not step == self.steps.first:
            kwargs['organization'] = self.request.user.profile.organization
        return kwargs

    def done(self, form_list, **kwargs):
        """
        Сохраняем все формы
        """
        client = None
        for form in form_list:
            if isinstance(form, forms.ClientForm) or isinstance(form, forms.ClientPassportForm):
                if not form.cleaned_data['client_code']:
                    client = form.save()
                else:
                    client = form.cleaned_data['client_code']
            elif isinstance(form, forms.AddConsultationForm):
                obj = form.save(client=client)
                for i in form.cleaned_data['sent_to']:
                    models.Direction.objects.create(consultation=obj, social_service=i, status=None)
            elif isinstance(form, forms.AddCertificateForm):
                obj = form.save(client=client)
            elif isinstance(form, forms.AddBlankForm):
                obj = form.save(client=client)
        return HttpResponseRedirect(obj.get_absolute_url())

named_consultation_forms = (
    ('add_client', forms.ClientForm),
    ('add_consultation', forms.AddConsultationForm),
)

cons_wizard = ClientWizard.as_view(named_consultation_forms,
    template_name = "consulatation/consultation_form.html",
    url_name='blank_step')

named_certificate_forms = (
    ('add_passport', forms.ClientPassportForm),
    ('add_certificate', forms.AddCertificateForm),
)

certificate_wizard = ClientWizard.as_view(named_certificate_forms,
    template_name = "certificate/certificate_form.html",
    url_name='blank_step')

named_blank_forms = (
    ('add_passport', forms.ClientPassportForm),
    ('add_blank', forms.AddBlankForm),
)

blank_wizard = ClientWizard.as_view(named_blank_forms,
    template_name = "blank/form.html",
    url_name='blank_step')