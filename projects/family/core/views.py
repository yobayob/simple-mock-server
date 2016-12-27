# -*- coding: utf-8 -*-

from datetime import datetime, timedelta

from django.contrib.auth import logout, authenticate, login
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import redirect
from django.views.generic import *
from django.core.validators import validate_email
from django.template import Context
from django.template.loader import get_template
from django.db.models import Q
from tasks import *
from xhtml2pdf import pisa
from os.path import join, isfile
from core.forms import *
from core.models import *
from django.core.exceptions import PermissionDenied as Http403
from pytils.dt import ru_strftime
import simplejson
import cStringIO


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
                        'keywords':self.keywords
                        })
        return context


# Template Views

class IndexView(TemplateMixin, TemplateView):
    template_name = 'index.html'


class HomeView(TemplateMixin, TemplateView):
    template_name = 'home.html'
    title = u'ГИМЦ “Семья”'


class OrgsView(TemplateMixin, TemplateView):
    template_name = 'orgs/list.html'
    model = Orgs

    def get_context_data(self, **kwargs):
        context = super(OrgsView, self).get_context_data(**kwargs)
        typeorgs = TypeOrgs.objects.exclude(orgs__isnull=True)
        context['typeorgs']=typeorgs
        return context


class ConsultationArchiveView(TemplateMixin, TemplateView):
    template_name = 'consulatation/consultation_archive.html'
    title = u'Архив консультаций'


class ConsultationView(TemplateMixin, TemplateView):
    template_name = 'consulatation/consultation_list.html'
    title = u'Просмотр консультации'


class RedirectionView(TemplateMixin, TemplateView):
    template_name = 'consulatation/redirection.html'
    title = u'Перенаправление клиентов'


class LegislationView(TemplateMixin, TemplateView):
    template_name = 'legislation.html'
    title = u'Законодательство'


class EventView(TemplateMixin, TemplateView):
    template_name = 'orgs/eventlist.html'
    title = u'Календарь мероприятий'


class SeatView(TemplateMixin, TemplateView):
    template_name = 'orgs/seatlist.html'
    title = u'Таблица свободных мест'


class MapView(TemplateMixin, TemplateView):
    template_name = 'map.html'
    title = u'Система комплексной реабилитации наркозависимых в Санкт-Петербурге'

    def get_context_data(self, **kwargs):
        context = super(MapView, self).get_context_data(**kwargs)
        typeorgs = TypeOrgs.objects.exclude(orgs__isnull=True)
        context['typeorgs']=typeorgs
        return context


class ComposeMessage(TemplateMixin, FormView):
    form_class = ComposeForm
    template_name = 'django_messages/compose.html'
    
    def get_form_kwargs(self):
        kwargs = super(ComposeMessage, self).get_form_kwargs()
        pk = self.kwargs.get('pk')
        if pk:
            kwargs.update({
                'user': User.objects.get(pk=pk)
            })
        return kwargs
        
    
    def form_valid(self, form):
        form.save(sender=self.request.user)
        return HttpResponseRedirect(reverse('messages_inbox'))
    
# Detail Views

class CreateBlankServiceItemView(TemplateMixin, CreateView):
    model = BlankServiceItem
    template_name = 'profile/social_service_form.html'
    title = u'Добавить услугу'
    fields = ['name', 'form_of_provision', 'description']

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.organization = self.request.user.profile.organization
        obj.save()
        return HttpResponseRedirect(reverse('user_profile', kwargs={'pk':self.request.user.profile.pk}))


class ProfileView(TemplateMixin, DetailView):
    model = Profile
    title = u'Профиль'

    def get_object(self, queryset=None):
        q = Profile.objects.get(user=self.request.user)
        return q

    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs)
        contacts = Contact.objects.filter(
            content_type = ContentType.objects.get(app_label='core', model='orgs'),
            object_id = context['object'].organization.id
        ).order_by('contact_type')
        events = Event.objects.filter(date__gt=datetime.today(), organization=context['object'].organization).order_by(
            'date')  # Показывает, только будущие мероприятия
        context.update({
            'contacts': contacts,
            'events': events,
        })
        return context


class UserProfileListView(TemplateMixin, ListView):
    model = Profile
    title = u'Специалисты'
    template_name = u'blank/users/list.html'


class UserProfileView(ProfileView):
    template_name = u'blank/users/detail.html'
    title = u'Профиль пользователя'

    def get_object(self, queryset=None):
        if self.kwargs.get('pk') is None:
            q = Profile.objects.get(user=self.request.user)
        else:
            q = Profile.objects.get(pk=self.kwargs.get('pk'))
        return q


class UserUpdateView(TemplateMixin, UpdateView):
    template_name = 'profile/social_service_form.html'
    model = Profile
    form_class = UserProfileForm

    def get_form_kwargs(self):
        kw = super(UserUpdateView, self).get_form_kwargs()
        kw.update({
            'profile':self.object
        })
        return kw

    def get_object(self, queryset=None):
        q = Profile.objects.get(user=self.request.user)
        return q

    def form_valid(self, form):
        obj = form.save()
        return HttpResponseRedirect(obj.get_absolute_url())


class CertificateDetailView(TemplateMixin, DetailView):
    template_name = 'certificate/certificate_detail.html'
    model = CertificateForPatients

    def get_title(self):
        return self.object


class OrgDetailView(TemplateMixin, DetailView):
    template_name = 'orgs/detail.html'
    model = Orgs

    def get_title(self):
        return self.object

class ConsultationDetailView(TemplateMixin, DetailView):
    model = Consultation
    template_name = "consulatation/consultation_detail.html"

    def get_title(self):
        return self.object


class EventDetailView(TemplateMixin, DetailView):
    template_name = 'event.html'
    model = Event

    def get_title(self):
        return self.object


class LegislationDocsView(TemplateMixin, DetailView):
    template_name = 'consulatation/docs.html'
    model = Legislation

    def get_title(self):
        return self.object


class SocialServiceDetailView(TemplateMixin, DetailView):
    template_name = "rcenter/detail.html"

    def get_title(self):
        return self.object


class MSDetailView(TemplateMixin, DetailView):
    template_name = 'rcenter/ms.html'
    model = MS

    def get_title(self):
        return self.object


class BlankListView(TemplateMixin, ListView):
    template_name = 'blank/list.html'
    model = Blank

    def get_queryset(self):
        qs = Blank.objects.filter(organization=self.request.user.profile.organization)
        return qs

class BlankDetailView(TemplateMixin, DetailView):
    template_name = 'blank/detail.html'
    model = Blank


class CloseCertificateView(TemplateMixin, DetailView):
    model = CertificateForPatientsStep
    template_name = "certificate/close_certificate_step.html"
    title = u'Погасить купон'

    def post(self, request, pk):
        try:
            obj = CertificateForPatientsStep.objects.get(pk=pk)
            organization = Profile.objects.get(user=request.user).organization
            if obj.certificate.social_service.org == organization:
                if obj.can_close():
                    obj.status = CERT_STEP_1
                    obj.save()
                    return HttpResponseRedirect('/certificate/' + str(obj.certificate.id))
            return HttpResponse('Не может быть погашено')
        except:
            return HttpResponse("Что-то пошло не так", status=500)


class BlankServicePlanDetailView(TemplateMixin, DetailView):
    model = BlankServicePlan
    title = u"Услуга"
    template_name = "blank/service/detail.html"

# Form Views


class AddFamilyMemberFormView(TemplateMixin, CreateView):
    model = FamilyMember
    form_class = FamilyMemberForm
    title = u"Добавить члена семьи"
    template_name = "profile/social_service_form.html"

    def get_blank(self):
        blank = Blank.objects.get(pk=self.kwargs.get('pk'))
        if blank.organization != self.request.user.profile.organization:
            raise Http403()
        return blank

    def form_valid(self, form):
        obj = form.save()
        return HttpResponseRedirect(obj.blank.get_absolute_url())

    def get_form_kwargs(self):
        kw = super(AddFamilyMemberFormView, self).get_form_kwargs()
        kw.update({
            'blank': self.get_blank()
        })
        return kw


class AddServiceFormView(TemplateMixin, CreateView):
    template_name = "profile/social_service_form.html"
    title = u'Добавить услугу'
    form_class = AddServiceForm

    def get_form_kwargs(self):
        kwargs = super(AddServiceFormView, self).get_form_kwargs()
        user = Profile.objects.get(user=self.request.user)
        socialservices = SocialService.objects.filter(org=user.organization)
        kwargs['queryset']= socialservices
        return kwargs

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(reverse('profile'))


class AddBlankServicePlanFormView(TemplateMixin, CreateView):
    template_name = "profile/social_service_form.html"
    title = u'Добавить услугу в план обслуживания'
    form_class = BlankServicePlanForm

    def get_form_kwargs(self):
        blank = Blank.objects.get(pk=self.kwargs.get('blank'))
        self.success_url = blank.get_absolute_url()
        if blank.organization != self.request.user.profile.organization:
            raise Http403()
        kwargs = super(AddBlankServicePlanFormView, self).get_form_kwargs()
        kwargs.update({
            'blank': blank,
            'user': self.request.user
        })
        return kwargs


class AddBlankServiceFormView(TemplateMixin, CreateView):
    template_name = "profile/social_service_form.html"
    title = u'Добавить услугу'
    form_class = BlankServiceForm

    def get_service_plan(self):
        service_plan = BlankServicePlan.objects.get(pk=self.kwargs.get('pk'))
        if service_plan.user != self.request.user:
            raise Http403("")
        return service_plan

    def get_form_kwargs(self):
        kwargs = super(AddBlankServiceFormView, self).get_form_kwargs()
        service_plan = self.get_service_plan()
        kwargs.update({
            'service_plan': service_plan
        })
        return kwargs

    def form_valid(self, form):
        # todo check date from start & end date plan
        obj = form.save()
        return HttpResponseRedirect(obj.service_plan.blank.get_absolute_url())


class AddSeatFormView(TemplateMixin, CreateView):
    template_name = "profile/social_service_form.html"
    form_class = AddSeatForm
    title = u'Обновить сведения о местах'

    def get_form_kwargs(self):
        kwargs = super(AddSeatFormView, self).get_form_kwargs()
        user = Profile.objects.get(user=self.request.user)
        socialservices = SocialService.objects.filter(org=user.organization, type__have_seat=True)
        kwargs['queryset'] = socialservices
        return kwargs

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(reverse('profile_seat'))


class AddSocialServiceView(TemplateMixin, CreateView):
    template_name = "profile/social_service_form.html"
    form_class = AddSocialServiceForm
    model = SocialService
    title = u'Добавить подразделение'

    def get_form_kwargs(self, **kwargs):
        kwargs = super(AddSocialServiceView, self).get_form_kwargs(**kwargs)
        kwargs['organization'] = Profile.objects.get(user=self.request.user).organization
        return kwargs

    def form_valid(self, form):
        obj = form.save()
        return HttpResponseRedirect(obj.get_absolute_url())


class AddEventVFormView(TemplateMixin, FormView):
    template_name = "profile/social_service_form.html"
    form_class = AddEventForm
    title = u'Добавить мероприятие'

    def get_form_kwargs(self):
        kwargs = super(AddEventVFormView, self).get_form_kwargs()
        kwargs['organization'] = Profile.objects.get(user=self.request.user).organization
        return kwargs

    def form_valid(self, form):
        obj = form.save()
        return HttpResponseRedirect(reverse('event_detail', kwargs={'pk': obj.pk}))


class CertificateView(TemplateMixin, FormView):
    template_name = "certificate/certificate_list.html"
    form_class = CloseCertificateForm
    title = u'Просмотр сертфиката'

    def form_valid(self, form):
        try:
            organization = Profile.objects.get(user=self.request.user).organization
            obj = CertificateForPatientsStep.objects.get(id=self.request.POST['code'])
            if obj.certificate.social_service.org == organization:
                if obj.can_close():
                    obj.status = CERT_STEP_1
                    obj.save()
                    return HttpResponse('Погашено')
            else: HttpResponse('Вы не можете погасить данный сертификат')
            return HttpResponse('Не может быть погашено')
        except:
            return HttpResponse("Данный код не зарегистрирован", status=404)


class AddCertificateFormView(TemplateMixin, FormView):
    template_name = "certificate/certificate_form.html"
    success_url = '/certificate/'
    form_class = AddCertificateForm
    title = u'Выдать сертификат'

    def get(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            return HttpResponse("Вы не можете выдавать сертификаты", status=403)
        form = self.get_form()
        return self.render_to_response(self.get_context_data(form=form))

    def get_form_kwargs(self):
        kwargs = super(AddCertificateFormView, self).get_form_kwargs()
        kwargs.update({
            'organization': Profile.objects.get(user=self.request.user).organization
        })
        return kwargs

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect('/certificate/')

    def form_invalid(self, form):
        error_message = dict([(key, [unicode(error) for error in value]) for key, value in form.errors.items()])
        return HttpResponse(simplejson.dumps({"result": error_message, }), content_type='application/json')


class AddConsultationFormView(TemplateMixin, FormView):
    template_name = "consulatation/consultation_form.html"
    success_url = '/consultation/'
    form_class = AddConsultationForm
    title = u'Добавить консультацию'

    def get_form_kwargs(self):
        kwargs = super(AddConsultationFormView, self).get_form_kwargs()
        kwargs.update({
            'organization': Profile.objects.get(user=self.request.user).organization
        })
        return kwargs

    def form_valid(self, form):
        patient = form.cleaned_data['patient']
        new_patient = {'first_name': form.cleaned_data['first_name'],
                       'middle_name': form.cleaned_data['middle_name'],
                       'last_name':form.cleaned_data['last_name'],
                       'sex': form.cleaned_data['sex'],
                       'birth_date': form.cleaned_data['birth_date']}
        if (not patient and form.cleaned_data['first_name']) or patient:
            obj = form.save(**new_patient)
            for i in form.cleaned_data['sent_to']:
                Direction.objects.create(consultation=obj, social_service=i, status=None)
            return HttpResponseRedirect('/consultation/' + str(obj.id))
        else:
            return Http404('Нет клиента')

    def form_invalid(self, form):
        error_message = dict([(key, [unicode(error) for error in value]) for key, value in form.errors.items()])
        return HttpResponse(simplejson.dumps({"result": error_message, }), content_type='application/json')


class SendEventNotificationFormView(FormView):
    template_name = 'form/standart.html'
    form_class = SendEventNotificationForm

    def form_valid(self, form):
        if not self.request.user.is_superuser:
            raise Http404(u"Пользователь не является администратором")
        mail = []
        users = Profile.objects.filter(notification_event=True)
        for user in users:
            if user.user.email:
                mail.append(user.user.email)
        if form.cleaned_data['mail']:
            mails = form.cleaned_data['mail']
            for m in mails.replace(" ", ";").replace(",", ";").split(";"):
                try:
                    validate_email(m)
                    mail.append(m)
                except forms.ValidationError:
                    pass
        send_mail_task.delay(form.cleaned_data['head'], form.cleaned_data['text'], mail)
        return HttpResponse("RELOAD")

    def get_form_kwargs(self):
        kwargs = super(SendEventNotificationFormView, self).get_form_kwargs()
        kwargs.update({
            'event': self.kwargs['pk'],
        })
        return kwargs


class AddMSFormView(TemplateMixin, CreateView):
    template_name = "profile/social_service_form.html"
    form_class = AddMSForm
    model = MS
    title = u'Добавить мобильную службу'

    def get_form_kwargs(self, **kwargs):
        kwargs = super(AddMSFormView, self).get_form_kwargs(**kwargs)
        kwargs['organization'] = Profile.objects.get(user=self.request.user).organization
        return kwargs

    def form_valid(self, form):
        obj = form.save()
        return HttpResponseRedirect(reverse('profile'))


class UpdateMSFormView(TemplateMixin, UpdateView):
    template_name = "profile/social_service_form.html"
    form_class = AddMSForm
    model = MS
    title = u'Редактировать данные мобильной службы'
    success_url = "/profile/"

    def get_object(self, queryset=None):
        object = super(UpdateMSFormView, self).get_object()
        organization = Profile.objects.get(user=self.request.user).organization
        if organization != object.org:
            raise Http403()
        return object

    def get_form_kwargs(self):
        kwargs = super(UpdateMSFormView, self).get_form_kwargs()
        kwargs.update({
            'organization':self.object.org,
            'mail':self.object.mail,
            'phone':self.object.phone,
        })
        return kwargs


class AddRouteMSFormView(TemplateMixin, CreateView):
    template_name = "profile/social_service_form.html"
    form_class = AddRouteMSForm
    model = MS
    title = u'Добавить точку маршрута'

    def get_object(self, queryset=None):
        obj = MS.objects.get(pk=self.kwargs['pk'])
        if obj.org != Profile.objects.get(user=self.request.user).organization:
            raise Http403()
        return obj

    def get_form_kwargs(self):
        kwargs = super(AddRouteMSFormView, self).get_form_kwargs()
        ms = self.get_object()
        kwargs.update({
            'ms':ms,
        })
        return kwargs

    def form_valid(self, form):
        obj = form.save()
        return HttpResponseRedirect(reverse('ms_detail', kwargs={'pk':obj.ms.pk}))


class UpdateRouteMSFormView(TemplateMixin, UpdateView):
    template_name = "profile/social_service_form.html"
    form_class = AddRouteMSForm
    model = RouteMS
    title = u'Редактировать точку маршрута'

    def get_object(self):
        obj = super(UpdateRouteMSFormView, self).get_object()
        if obj.ms.org != Profile.objects.get(user=self.request.user).organization:
            raise Http403()
        return obj

    def get_form_kwargs(self):
        kwargs = super(UpdateRouteMSFormView, self).get_form_kwargs()
        ms = self.object.ms
        kwargs.update({
            'ms':ms,
        })
        return kwargs

    def form_valid(self, form):
        obj = form.save()
        return HttpResponseRedirect(reverse('ms_detail', kwargs={'pk':obj.ms.pk}))

# Create Views

class JoinFormView(TemplateMixin, CreateView):
    template_name = 'form.html'
    form_class = OrgsForm
    title = u'Система перенаправления клиентов'

    def get_context_data(self, **kwargs):
        from public.models import FlatPage, PAGE_FORM
        context = super(JoinFormView, self).get_context_data(**kwargs)
        context['public'] = True
        if 'success' in self.kwargs:
            context['success']=True
        if FlatPage.objects.filter(type=PAGE_FORM).exists():
            context.update({
                'object': FlatPage.objects.get(type=PAGE_FORM),
            })
        return context

    def form_valid(self, form):
        obj = form.save()
        head = 'Новая заявка на регистрацию в системе'
        text = """Поступила новая заявка на регистрацию в системе.
Подробности - https://srnzspb.ru/admin/core/orgs/%d/
        """ % obj.pk
        mail = 'depeduspb@gmail.com'
        send_mail_task.delay(head, text, [mail])
        return HttpResponseRedirect(reverse('form_success'))


class AddPatientView(TemplateMixin, CreateView):
    template_name = 'form/standart.html'
    model = Patient
    fields = "__all__"
    title = u'Добавить клиента '

    def get_form(self, form_class=None):
        form = super(AddPatientView, self).get_form(form_class)
        for field in form.fields:
            form.fields[field].widget.attrs['class'] = 'form-control'
            form.fields[field].widget.attrs['ng-model'] = 'form.' + field
        return form

    def form_valid(self, form):
        form.save()
        return HttpResponse('RELOAD')

    def form_invalid(self, form):
        error_message = dict([(key, [unicode(error) for error in value]) for key, value in form.errors.items()])
        return HttpResponse(simplejson.dumps({"result": error_message, }), content_type='application/json')


class AddPatientDinamicView(TemplateMixin, CreateView):
    template_name = 'form/addPatient.html'
    model = Patient
    fields = "__all__"
    title = u'Добавить клиента'

    def get_form(self, form_class=None):
        form = super(AddPatientDinamicView, self).get_form(form_class)
        for field in form.fields:
            form.fields[field].widget.attrs['class'] = 'form-control'
            form.fields[field].widget.attrs['ng-model'] = 'form.' + field
        return form

    def form_valid(self, form):
        obj = form.save()
        answer = [{
                    "patient":{
                        "name": obj.name(),
                        "id":obj.id
                    }
                }]
        return HttpResponse(simplejson.dumps(answer), content_type='application/json')

    def form_invalid(self, form):
        error_message = dict([(key, [unicode(error) for error in value]) for key, value in form.errors.items()])
        print error_message
        return HttpResponse(simplejson.dumps({"result": error_message, }), content_type='application/json')


class CreateContactView(TemplateMixin, CreateView):
    model = Contact
    fields = ('contact_type', 'contact_value')
    template_name = 'form/standart.html'
    title = u'Создание контакта'

    def get_form(self, form_class=None):
        form = super(CreateContactView, self).get_form(form_class)
        for field in form.fields:
            form.fields[field].widget.attrs['ng-model'] = 'form.' + field
            form.fields[field].widget.attrs[
                'ng-Initial'] = ''  # Костыль, чтобы не сбрасывалось значение при редактировании
        return form

    def form_valid(self, form):
        content_type = ContentType.objects.get(app_label='core', model='orgs')
        obj = form.save(commit=False)
        obj.content_type = content_type
        obj.object_id = self.request.user.profile.organization.id
        obj.save()
        return HttpResponse('RELOAD')

    def form_invalid(self, form):
        error_message = dict([(key, [unicode(error) for error in value]) for key, value in form.errors.items()])
        return HttpResponse(simplejson.dumps({"result": error_message, }), content_type='application/json')

# Update Views

class UpdateEvent(TemplateMixin, UpdateView):
    model = Event
    template_name = "profile/social_service_form.html"
    form_class = AddEventForm
    title = u'Обновить данные о мероприятии'

    def get_form(self, form_class=None):
        organization = Profile.objects.get(user=self.request.user).organization
        if organization != self.object.organization:
            raise Http404("Вы не можете редактировать указанное мероприятие")
        form = super(UpdateEvent, self).get_form(form_class)
        return form

    def get_form_kwargs(self):
        kwargs = super(UpdateEvent, self).get_form_kwargs()
        kwargs['organization'] = self.request.user.profile.organization
        return kwargs

    def form_valid(self, form):
        obj = form.save()
        return HttpResponseRedirect(reverse('event_detail', kwargs={'pk':obj.pk}))


class UpdateService(TemplateMixin, UpdateView):
    model = SocialServiceItem
    form_class = AddServiceForm
    template_name = "profile/social_service_form.html"
    title = u'Обновить сведения об услуге'

    def get_object(self, queryset=None):
        object = super(UpdateService, self).get_object()
        organization = Profile.objects.get(user=self.request.user).organization
        if organization != object.social_service.org:
            raise Http403()
        return object

    def get_form_kwargs(self):
        kwargs = super(UpdateService, self).get_form_kwargs()
        kwargs['queryset'] = SocialService.objects.filter(org=self.request.user.profile.organization)
        return kwargs

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(reverse('profile_service'))


class UpdateSocialService(TemplateMixin, UpdateView):
    model = SocialService
    form_class = AddSocialServiceForm
    template_name = "profile/social_service_form.html"
    success_url = "/profile/"
    title = u'Обновить данные подразделения'

    def get_object(self, queryset=None):
        object = super(UpdateSocialService, self).get_object()
        organization = Profile.objects.get(user=self.request.user).organization
        if organization != object.org:
            raise Http403()
        return object

    def get_form_kwargs(self):
        kwargs = super(UpdateSocialService, self).get_form_kwargs()
        kwargs.update({
            'organization':self.object.org,
            'mail':self.object.mail,
            'phone':self.object.phone,
        })
        return kwargs


class UpdateOrg(TemplateMixin, UpdateView):
    model = Orgs
    success_url = '/profile/'
    template_name = "profile/social_service_form.html"
    form_class = FullOrgsForm
    title = u'Обновить данные организации'

    def get_object(self, queryset=None):
        q = Profile.objects.get(user=self.request.user).organization
        return q

    def get_form_kwargs(self):
        kwargs = super(UpdateOrg, self).get_form_kwargs()
        kwargs.update({
            'phone':self.object.phone,
            'mail':self.object.mail,
        })
        return kwargs


class UpdateConsultation(TemplateMixin, UpdateView):
    model = Direction
    fields = ['status']
    template_name = "form/standart.html"
    title = u'Редактирование консультации'

    def get_object(self, queryset=None):
        object = super(UpdateConsultation, self).get_object()
        organization = Profile.objects.get(user=self.request.user).organization
        if organization != object.social_service.org:
            raise Http403()
        return object

    def get_form(self, form_class=None):
        form = super(UpdateConsultation, self).get_form(form_class)
        for field in form.fields:
             form.fields[field].widget.attrs.update({
                 'class':'form-control',
                 'ng-model': 'form.' + field,
                 'ng-Initial': '',
             })
        return form

    def form_valid(self, form):
        form.save()
        return HttpResponse('RELOAD')

    def form_invalid(self, form):
        error_message = dict([(key, [unicode(error) for error in value]) for key, value in form.errors.items()])
        return HttpResponse(simplejson.dumps({"result": error_message, }), content_type='application/json')


class UpdateContactView(TemplateMixin, UpdateView):
    model = Contact
    fields = ('contact_value',)
    template_name = 'form/standart.html'
    title = u'Редактирование контактов'

    def form_valid(self, form):
        form.save()
        return HttpResponse('RELOAD')

    def get_form(self, form_class=None):
        form = super(UpdateContactView, self).get_form(form_class)
        for field in form.fields:
            form.fields[field].widget.attrs['ng-model'] = 'form.' + field
            form.fields[field].widget.attrs[
                'ng-Initial'] = ''  # Костыль, чтобы не сбрасывалось значение при редактировании
        return form

    def form_invalid(self, form):
        error_message = dict([(key, [unicode(error) for error in value]) for key, value in form.errors.items()])
        return HttpResponse(simplejson.dumps({"result": error_message, }), content_type='application/json')

class UpdateCertificateView(TemplateMixin, UpdateView):
    model = CertificateForPatients
    fields = ('status', 'date_end', 'date_start')
    template_name = "profile/social_service_form.html"
    title = u'Изменить сертификат'


# PDF Views

# Convert HTML URIs to absolute system paths so xhtml2pdf can access those resources
def link_callback(uri, rel):
    # use short variable names
    sUrl = settings.STATIC_URL      # Typically /static/
    sRoot = settings.STATIC_ROOT    # Typically /home/userX/project_static/
    mUrl = settings.MEDIA_URL       # Typically /static/media/
    mRoot = settings.MEDIA_ROOT     # Typically /home/userX/project_static/media/

    # convert URIs to absolute system paths
    if uri.startswith(mUrl):
        path = join(mRoot, uri.replace(mUrl, ""))
    elif uri.startswith(sUrl):
        path = join(sRoot, uri.replace(sUrl, ""))
    else:
        return uri # handle absolute uri (ie: http://some.tld/foo.png)

    # make sure that file exists
    if not isfile(path):
            raise Exception(
                    'media URI must start with %s or %s' % \
                    (sUrl, mUrl))
    return path


class ConsultationPdfView(View):
    def get(self, request, pk):
        obj = Consultation.objects.get(pk=pk)
        template = get_template('pdf/consultation.html')
        html  = template.render(Context({'object':obj}))
        filename = "consultation_%s.pdf" % (obj.id)
        file = open(join(settings.MEDIA_ROOT,"temp",filename), "w+b")
        pisaStatus = pisa.CreatePDF(cStringIO.StringIO(html.encode('utf-8')), dest=file, link_callback = link_callback, encoding='utf-8')
        file.seek(0)
        pdf = file.read()
        file.close()            # Don't forget to close the file handle
        return HttpResponse(pdf, content_type='application/pdf')


class CertificatePdfView(View):
    def get(self, request, pk):
        obj = CertificateForPatients.objects.get(pk=pk)
        template = get_template('pdf/certificate.html')
        html  = template.render(Context({'object':obj}))
        filename = "certificate_%s.pdf" % (obj.id)
        file = open(join(settings.MEDIA_ROOT,"temp",filename), "w+b")
        pisaStatus = pisa.CreatePDF(cStringIO.StringIO(html.encode('utf-8')), dest=file, link_callback = link_callback, encoding='utf-8')
        file.seek(0)
        pdf = file.read()
        file.close()            # Don't forget to close the file handle
        return HttpResponse(pdf, content_type='application/pdf')


# LOGIN

class LogOutView(View):
    def get(self, request):
        logout(request)
        return redirect('/')


class LoginView(View):
    def post(self, request):
        print 'post'
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponse('OK')
            HttpResponse(u'Пользователь не активен', status=403)
        return HttpResponse(u'Некорректный логин/пароль', status=403)


# Delete

class DeleteContactView(View):
    """
    Удаление контактов
    """
    def get(self, request, pk):
        contact = Contact.objects.get(pk=pk)
        if contact.object_id == request.user.profile.organization.id: contact.delete()
        return HttpResponseRedirect(reverse('profile'))



class ReportView(TemplateMixin, TemplateView):
    template_name = 'reports.html'

    def get_context_data(self, **kwargs):
        context = super(ReportView, self).get_context_data(**kwargs)
        context.update({'data':[{
                'name':'Организации',
                'labels':['Всего', 'Новых'],
                'count': Orgs.objects.all().count(),
                'new': Orgs.objects.filter(created__gte=datetime.today()-timedelta(days=30)).count()
                },{
                'name':'Пользователи системы',
                'labels':['Всего', 'Новых'],
                'count': Profile.objects.all().count(),
                'new': Profile.objects.filter(created__gte=datetime.today()-timedelta(days=30)).all().count()
                },{
                'name':'Учетные карты',
                'labels':['Всего', 'Новых'],
                'count':Blank.objects.all().count(),
                'new': Blank.objects.filter(created__gte=datetime.today()-timedelta(days=30)).all().count()
                 },{
                'name':'Консультации',
                'labels':['Всего', 'Новых'],
                'count': Consultation.objects.all().count(),
                'new': Consultation.objects.filter(created__gte=datetime.today()-timedelta(days=30)).all().count()
                }]}
        )
        return context

# JSON

class OrgsJson(View):
    def get(self, request):
        obj = Orgs.objects.filter(status=ORG_STATUS_APPROVED)
        answer = [{'id': i.id,
                   'site': i.site,
                   'full_name': i.full_name,
                   'phone': i.phone,
                   'name': i.name,
                   'address': i.coor_address,
                   'inn': i.inn,
                   'orgn': i.orgn,
                   'mail': i.mail,
                   'type': i.type.name,
                   'coor_x': i.coor_x,
                   'coor_y': i.coor_y,
                   } for i in obj
                  ]
        return HttpResponse(simplejson.dumps(answer), content_type='application/json')


class SocialServiceJson(View):
    def get(self, request):
        qs_filters = {}
        filters = {
                  'organization': 'org__pk',
                  'type': 'type__name',
              }
        for filter_name, qs_filter in filters.iteritems():
          filter_val = request.GET.get(filter_name)
          if filter_val:
            qs_filters[qs_filter] = filter_val
        obj = SocialService.get_approved().filter(**qs_filters)
        answer = [{'id': i.id,
                   'name': i.name,
                   'address': i.address,
                   'phone': i.phone,
                   'mail': i.mail,
                   'description': i.description,
                   'type': i.type.name,
                   'coor_x': i.coor_x,
                   'coor_y': i.coor_y,
                   } for i in obj
                  ]
        return HttpResponse(simplejson.dumps(answer), content_type='application/json')


class EventJson(View):
    def get(self, request):
        obj = Event.objects.filter(date__gt=datetime.today()).order_by('date')  # Показывает, только будущие мероприятия
        answer = [{'id': i.id,
                   'date': ru_strftime("%d %B %Y %H:%M", date=i.date, inflected=True),
                   'org_id': i.organization.id,
                   'org': i.organization.name,
                   'name': i.name,
                   'address': i.address,
                   'participant': i.participant,
                   'description': i.description,
                   } for i in obj
                  ]
        return HttpResponse(simplejson.dumps(answer), content_type='application/json')


class SeatJson(View):
    def get(self, request):
        answer = list()
        obj = SocialService.objects.filter(type__have_seat=True)
        for i in obj:
            if Seat.objects.filter(social_service=i).exists():
                seat = Seat.objects.filter(social_service=i).latest('id')
                answer.append({
                    'name': i.name,
                    'all': seat.seats,
                    'men': seat.seats_for_men,
                    'woman': seat.seats_for_woman,
                    'date': ru_strftime("%d %B %Y", date=seat.created, inflected=True),
                })
        return HttpResponse(simplejson.dumps(answer), content_type='application/json')


class LegislationJson(View):
    def get(self, request):
        obj = Legislation.objects.all()
        answer = [
            {
                'id': i.id,
                'file': i.file.url,
                'name': i.name,
                'date': ru_strftime("%d %B %Y", date=i.date, inflected=True),
                'extension': i.extension(),
            } for i in obj
            ]
        return HttpResponse(simplejson.dumps(answer), content_type='application/json')


class ConsultationJson(View):
    def get(self, request):
        obj = Consultation.objects.filter(organization=request.user.profile.organization)
        answer = [
            {
                'id': i.id,
                'patient': i.patient.name,
                'patient_id': i.patient.id,
                'date': ru_strftime("%d %B %Y", date=i.date, inflected=True),
                'organization': i.organization.name,
                'sent_to': [j.social_service.name for j in i.sent_to()],
                'sent_to_text': i.sent_to_text,
            } for i in obj
            ]
        return HttpResponse(simplejson.dumps(answer), content_type='application/json')


class CertificateJson(View):
    def get(self, request):
        if request.user.is_superuser:
            obj = CertificateForPatients.objects.all()
        else:
            org = self.request.user.profile.organization
            obj = CertificateForPatients.objects.filter(Q(social_service__org=org) | Q(setter_org=org))
        answer = [
            {
                'id': i.id,
                #'patient': i.patient.name(),
                'step': i.step().get_step_display(),
                'organization': i.social_service.name,
                'date':i.date_end.strftime('%Y-%m-%d'),
            } for i in obj
            ]
        return HttpResponse(simplejson.dumps(answer), content_type='application/json')


class DirectionJson(View):
    def get(self, request):
        obj = Direction.objects.filter(social_service__org=request.user.profile.organization)
        answer = [
            {
                'id': i.id,
                'consultation_id': i.consultation.id,
                'patient': i.consultation.patient.name,
                'status':i.get_status_display(),
                'date': i.consultation.date.strftime('%Y-%m-%d'),
                'organization':i.consultation.organization.name,
            } for i in obj
            ]
        return HttpResponse(simplejson.dumps(answer), content_type='application/json')


class PatientJson(View):
    def get(self, request, pk):
        obj = Patient.objects.get(pk=pk)
        answer = {
                'id': obj.id,
                'name': obj.name,
                'sex':obj.sex
            }
        return HttpResponse(simplejson.dumps(answer), content_type='application/json')


class DebugCelery(View):
    def get(self, request):
        result = debug_celery.delay()
        return HttpResponse(str(result.wait()))