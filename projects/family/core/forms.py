# -*- coding: utf-8 -*-
from django import forms
from core.models import *
from django.contrib.admin.widgets import AdminFileWidget
from django.forms.widgets import HiddenInput, FileInput
from family.settings import SITE_URL
from django.utils.translation import ugettext_lazy as _

class AttrFormMixin(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(forms.ModelForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['ng-initial'] = ''
            self.fields[field].widget.attrs['ng-model'] = 'main.' + field
            if (self.fields[field].required and type(self.fields[field].widget) not in (AdminFileWidget, HiddenInput, FileInput) and '__prefix__' not in self.fields[field].widget.attrs):
                self.fields[field].widget.attrs['required'] = 'required'
                if self.fields[field].label:
                        self.fields[field].label += ' *'
            if isinstance(self.fields[field], forms.fields.BooleanField):
                continue
            elif isinstance(self.fields[field], (forms.fields.MultipleChoiceField, forms.models.ModelMultipleChoiceField,forms.models.ModelChoiceField, forms.fields.ChoiceField)):
                self.fields[field].widget.attrs['class'] = 'selectize form-control'
                continue
            elif isinstance(self.fields[field], forms.fields.DateField):
                self.fields[field].widget.attrs['datepicker'] = ""
            self.fields[field].widget.attrs['class'] = 'form-control'


class ClientForm(AttrFormMixin):
    """
    Форма добавления клиентов
    """

    client_code = forms.ModelChoiceField(queryset=Patient.objects.all(), required=False, label="Выберите клиента *")

    class Meta:
        model = Patient
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ClientForm, self).__init__(*args, **kwargs)
        self.fields['client_code'].widget.attrs['selectize']=""
        self.fields['client_code'].widget.attrs['required']="True"
        self.fields['name'].widget.attrs['required']="True"
        for field in self.fields:
            self.fields[field].required = False


class ClientPassportForm(AttrFormMixin):

    client_code = forms.ModelChoiceField(queryset=Passport.objects.all(), required=False, label="Выберите клиента *")

    class Meta:
        model = Passport
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ClientPassportForm, self).__init__(*args, **kwargs)
        self.fields['client_code'].widget.attrs['selectize']=""
        for field in self.fields:
            self.fields[field].widget.attrs['required']="True"
            self.fields[field].required = False

class OrgsForm(AttrFormMixin):
    """
    Форма добавления услуг
    """
    address = forms.CharField(label=u'Адрес')
    phone = forms.CharField(label=u'Телефон')
    mail = forms.EmailField(label=u'Email')

    class Meta:
        model = Orgs
        fields = ['name', 'index', 'district', 'address', 'type', 'chief']

    def __init__(self, *args, **kwargs):
        super(OrgsForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['ng-model'] = 'form.' + field

    def save(self, force_insert=False, force_update=False, commit=True):
        from core.models import Contact, CONTACT_TYPE_EMAIL, CONTACT_TYPE_PHONE
        m = super(OrgsForm, self).save(commit=False)
        if commit:
            m.save()
            phone = Contact(
                content_object=m,
                contact_type=CONTACT_TYPE_PHONE,
                contact_value=self.cleaned_data['phone'],
            )
            phone.save()
            mail = Contact(
                content_object=m,
                contact_type=CONTACT_TYPE_EMAIL,
                contact_value=self.cleaned_data['mail'],
            )
            mail.save()
        return m


class FullOrgsForm(AttrFormMixin):
    """
    Форма редактирования организации
    """
    phone = forms.CharField(label=u'Телефон')
    mail = forms.EmailField(label=u'Email')

    class Meta:
        model = Orgs
        exclude = ['coor_x', 'coor_y', 'status', 'is_certificate_for_patients', 'is_in_social_register', 'uuid', 'history']

    def __init__(self, *args, **kwargs):
        mail = kwargs.pop('mail')
        phone = kwargs.pop('phone')
        super(FullOrgsForm, self).__init__(*args, **kwargs)
        self.fields['mail'].initial = mail
        self.fields['phone'].initial = phone
        for field in self.fields:
            self.fields[field].widget.attrs['ng-model'] = 'form.' + field

    def save(self, force_insert=False, force_update=False, commit=True):
        # TODO наследоваться от формы выше
        from core.models import Contact, CONTACT_TYPE_EMAIL, CONTACT_TYPE_PHONE
        m = super(FullOrgsForm, self).save(commit=False)
        if commit:
            m.save()
            phone = Contact(
                content_object=m,
                contact_type=CONTACT_TYPE_PHONE,
                contact_value=self.cleaned_data['phone'],
            )
            phone.save()
            mail = Contact(
                content_object=m,
                contact_type=CONTACT_TYPE_EMAIL,
                contact_value=self.cleaned_data['mail'],
            )
            mail.save()
        return m


class UserProfileForm(AttrFormMixin):
    """
    Form edit user fields with contact and name
    """
    first_name = forms.CharField(label=u'Имя')
    last_name = forms.CharField(label=u'Фамилия')
    phone = forms.CharField(label=u'Телефон')
    mail = forms.EmailField(label=u'Email')

    class Meta:
        model = Profile
        exclude = ['user', 'organization']

    def __init__(self, *args, **kwargs):
        profile = kwargs.pop('profile')
        super(UserProfileForm, self).__init__(*args, **kwargs)
        self.fields['mail'].initial = profile.mail
        self.fields['phone'].initial = profile.phone
        self.fields['first_name'].initial = profile.user.first_name
        self.fields['last_name'].initial = profile.user.last_name
        for field in self.fields:
            self.fields[field].widget.attrs['ng-model'] = 'form.' + field

    def save(self, force_insert=False, force_update=False, commit=True):
        # TODO наследоваться от формы выше
        from core.models import Contact, CONTACT_TYPE_EMAIL, CONTACT_TYPE_PHONE
        m = super(UserProfileForm, self).save(commit=False)
        if commit:
            m.save()
            m.user.first_name = self.cleaned_data['first_name']
            m.user.last_name = self.cleaned_data['last_name']
            m.user.save()
            phone = Contact(
                content_object=m,
                contact_type=CONTACT_TYPE_PHONE,
                contact_value=self.cleaned_data['phone'],
            )
            phone.save()
            mail = Contact(
                content_object=m,
                contact_type=CONTACT_TYPE_EMAIL,
                contact_value=self.cleaned_data['mail'],
            )
            mail.save()
        return m


class AddSeatForm(AttrFormMixin):
    """
    Обновление данных о местах
    """
    class Meta:
        model = Seat
        fields = ['social_service','seats_for_men', 'seats_for_woman', 'seats']

    def __init__(self, *args, **kwargs):
        queryset = kwargs.pop('queryset', None)
        super(AddSeatForm, self).__init__(*args, **kwargs)
        if queryset:
            self.fields['social_service'].queryset = queryset
        for field in self.fields:
            self.fields[field].widget.attrs['ng-model'] = 'form.' + field


class AddServiceForm(AttrFormMixin):
    """
    Добавление услуг
    """
    class Meta:
        model = SocialServiceItem
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        queryset = kwargs.pop('queryset')
        super(AddServiceForm, self).__init__(*args, **kwargs)
        self.fields['social_service'].queryset = queryset
        for field in self.fields:
            self.fields[field].widget.attrs['ng-model'] = 'form.' + field


class AddEventForm(AttrFormMixin):
    """
    Добавление событий (календарь мероприятий)
    """

    class Meta:
        model = Event
        exclude = ['organization']

    def __init__(self, *args, **kwargs):
        self.organization = kwargs.pop('organization')
        super(AddEventForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
            self.fields[field].widget.attrs['ng-model'] = 'form.' + field

    def save(self):
        obj = super(AddEventForm, self).save(commit=False)
        obj.organization = self.organization
        obj.save()
        return obj


class AddSocialServiceForm(AttrFormMixin):
    """
    Добавление подразделений
    """

    address = forms.CharField(label=u'Адрес')
    phone = forms.CharField(label=u'Телефон')
    mail = forms.EmailField(label=u'Email')

    class Meta:
        model = SocialService
        exclude = ['org', 'coor_x', 'coor_y', 'seats', 'seats_for_men', 'seats_for_woman']

    def __init__(self, *args, **kwargs):
        self.organization = kwargs.pop('organization')
        mail = kwargs.pop('mail', None)
        phone = kwargs.pop('phone', None)
        super(AddSocialServiceForm, self).__init__(*args, **kwargs)
        self.fields['mail'].initial = mail
        self.fields['phone'].initial = phone
        for field in self.fields:
            self.fields[field].widget.attrs['ng-model'] = 'form.' + field     

    def save(self, force_insert=False, force_update=False, commit=True):
        from core.models import Contact, CONTACT_TYPE_EMAIL, CONTACT_TYPE_PHONE
        m = super(AddSocialServiceForm, self).save(commit=False)
        if commit:
            m.org = self.organization
            m.save()
            phone = Contact(
                content_object=m,
                contact_type=CONTACT_TYPE_PHONE,
                contact_value=self.cleaned_data['phone'],
            )
            phone.save()
            mail = Contact(
                content_object=m,
                contact_type=CONTACT_TYPE_EMAIL,
                contact_value=self.cleaned_data['mail'],
            )
            mail.save()
        return m


class AddMSForm(AttrFormMixin):
    """
    Добавление МС
    """

    address = forms.CharField(label=u'Адрес')
    phone = forms.CharField(label=u'Телефон')
    mail = forms.EmailField(label=u'Email')

    class Meta:
        model = SocialService
        exclude = ['org', 'coor_x', 'coor_y', 'seats', 'seats_for_men', 'seats_for_woman']

    def __init__(self, *args, **kwargs):
        self.organization = kwargs.pop('organization')
        mail = kwargs.pop('mail', None)
        phone = kwargs.pop('phone', None)
        super(AddMSForm, self).__init__(*args, **kwargs)
        if mail:
            self.fields['mail'].initial = mail
        if phone:
            self.fields['phone'].initial = phone
        for field in self.fields:
            self.fields[field].widget.attrs['ng-model'] = 'form.' + field

    def save(self, force_insert=False, force_update=False, commit=True):
        from core.models import Contact, CONTACT_TYPE_EMAIL, CONTACT_TYPE_PHONE
        m = super(AddMSForm, self).save(commit=False)
        if commit:
            m.org = self.organization
            m.save()
            phone = Contact(
                content_object=m,
                contact_type=CONTACT_TYPE_PHONE,
                contact_value=self.cleaned_data['phone'],
            )
            phone.save()
            mail = Contact(
                content_object=m,
                contact_type=CONTACT_TYPE_EMAIL,
                contact_value=self.cleaned_data['mail'],
            )
            mail.save()
        return m


class AddRouteMSForm(AttrFormMixin):
    """
    Добавление точки маршрута МС
    """

    class Meta:
        model = RouteMS
        exclude = ['ms', 'coor_x', 'coor_y']

    def __init__(self, **kwargs):
        self.ms = kwargs.pop('ms')
        super(AddRouteMSForm, self).__init__(**kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['ng-model'] = 'form.' + field

    def save(self, commit=True):
        m = super(AddRouteMSForm, self).save(commit=False)
        if commit:
            m.ms = self.ms
            m.save()
        return m


class AddConsultationForm(AttrFormMixin):
    """
    Форма для добавления консультаций
    """
    sent_to = forms.ModelMultipleChoiceField(label="Направлен", queryset=SocialService.objects.all(), required=False)

    def __init__(self, *args, **kwargs):
        self.organization = kwargs.pop('organization')
        super(AddConsultationForm, self).__init__(*args, **kwargs)

    def save(self, **kwargs):
        """
        Автоматическое добавление организации + добавление клиента, если требуется
        """
        patient = kwargs.pop('client')
        obj = super(AddConsultationForm, self).save(commit=False)
        obj.organization = self.organization
        obj.patient = patient
        obj.save()
        return obj

    class Meta:
        model = Consultation
        exclude = ['organization', 'status', 'id_in_organization', 'patient']


class AddPatientForm(AttrFormMixin):
    """
    Добавление пациентов
    """

    def __init__(self, *args, **kwargs):
        super(AddPatientForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['ng-model'] = 'form.' + field

    class Meta:
        model = Patient
        fields = '__all__'


class AddCertificateForm(AttrFormMixin):
    """
    Добавление сертификатов для пациентов
    """

    def __init__(self, *args, **kwargs):
        self.organization = kwargs.pop('organization')
        super(AddCertificateForm, self).__init__(*args, **kwargs)
        self.fields['social_service'].queryset = SocialService.objects.filter(org__is_certificate_for_patients=True)

    def save(self, **kwargs):
        patient = kwargs.pop('client')
        obj = super(AddCertificateForm, self).save(commit=False)
        obj.patient = patient
        obj.setter_org = self.organization
        obj.save()
        return obj


    class Meta:
        model = CertificateForPatients
        exclude = ['patient', 'status', 'setter_org']


class AddBlankForm(AttrFormMixin):
    """
    Добавление учетных карт
    """

    def __init__(self, *args, **kwargs):
        self.org = kwargs.pop('organization')
        super(AddBlankForm, self).__init__(*args, **kwargs)

    def save(self, **kwargs):
        patient = kwargs.pop('client')
        obj = super(AddBlankForm, self).save(commit=False)
        obj.patient = patient
        obj.organization = self.org
        obj.save()
        return obj


    class Meta:
        model = Blank
        exclude = ['patient', 'organization']


class BlankServicePlanForm(AttrFormMixin):
    """
    Добавление услуги в план обслуживания
    """

    class Meta:
        model = BlankServicePlan
        exclude = ['blank', 'user']

    def __init__(self, **kwargs):
        self.blank = kwargs.pop('blank')
        self.user = kwargs.pop('user')
        super(BlankServicePlanForm, self).__init__(**kwargs)
        self.fields['service'].queryset = BlankServiceItem.objects.filter(organization=self.user.profile.organization)

    def save(self, **kwargs):
        obj = super(BlankServicePlanForm, self).save(commit=False)
        obj.blank = self.blank
        obj.user = self.user
        obj.save()
        return obj


class BlankServiceForm(AttrFormMixin):
    """
    Услуги предоставляемые специалистами
    и учитываемые в бланках
    """

    class Meta:
        model = BlankService
        exclude = ['service_plan', 'cancelled_date', 'cancelled_reason']

    def __init__(self, **kwargs):
        self.service_plan = kwargs.pop('service_plan')
        super(BlankServiceForm, self).__init__(**kwargs)

    def save(self, **kwargs):
        obj = super(BlankServiceForm, self).save(commit=False)
        obj.service_plan = self.service_plan
        obj.save()
        return obj


class FamilyMemberForm(AttrFormMixin):

    class Meta:
        model = FamilyMember
        exclude = ['blank']

    def __init__(self, **kwargs):
        self.blank = kwargs.pop('blank')
        super(FamilyMemberForm, self).__init__(**kwargs)

    def save(self, **kwargs):
        obj = super(FamilyMemberForm, self).save(commit=False)
        obj.blank = self.blank
        obj.save()
        return obj


class CloseCertificateForm(forms.Form):
    """
    Погашение купона сертификата
    """

    code = forms.IntegerField(label=u'Код купона:')

    def __init__(self, *args, **kwargs):
        super(forms.Form, self).__init__(*args, **kwargs)
        self.fields['code'].widget.attrs['class'] = 'form-control'


class ComposeForm(forms.Form):
    """
    A simple default form for private messages.
    """
    recipient = forms.ModelChoiceField(queryset=User.objects.all(), label=_(u"Recipient"))
    subject = forms.CharField(label=_(u"Subject"), max_length=140)
    body = forms.CharField(label=_(u"Body"),
        widget=forms.Textarea(attrs={'rows': '12', 'cols':'55'}))

    def __init__(self, *args, **kwargs):
        kwargs.pop('recipient_filter', None)
        recipient = kwargs.pop('user', None)
        super(ComposeForm, self).__init__(*args, **kwargs)
        self.fields['recipient'].widget.attrs['class'] = 'selectize form-control'
        if recipient:
            self.fields['recipient'].initial = recipient

    def save(self, sender, parent_msg=None):
        from django_messages.models import Message
        from django.utils import timezone
        recipients = self.cleaned_data['recipient']
        subject = self.cleaned_data['subject']
        body = self.cleaned_data['body']
        message_list = []
        msg = Message(
            sender = sender,
            recipient = recipients,
            subject = subject,
            body = body,
        )
        if parent_msg is not None:
            msg.parent_msg = parent_msg
            parent_msg.replied_at = timezone.now()
            parent_msg.save()
        msg.save()
        message_list.append(msg)
        return message_list




class SendEventNotificationForm(forms.Form):
    """
    Отправка нотификаций о мероприятиях
    """
    head = forms.CharField(label=u'Тема рассылки')
    text = forms.CharField(label=u'Текст', widget=forms.Textarea)
    mail = forms.CharField(label=u'Дополнительные адреса для рассылки', widget=forms.Textarea, required=False)

    def __init__(self, *args, **kwargs):
        self.event = Event.objects.get(pk=kwargs.pop('event'))
        super(SendEventNotificationForm, self).__init__(*args, **kwargs)
        self.fields['head'].initial = u'Новое мероприятие: «%s»' % self.event.name
        self.fields['text'].initial = u'''Здравствуйте, уважаемый пользователь!

В «Электронной системе перенаправления клиентов регионального сегмента комплексной реабилитации лиц с наркотической зависимостью Санкт-Петербурга» добавлено новое мероприятие - «%s».

Подробности: %s

Методист: Смирнова Анастасия Алексеевна.
            ''' % (self.event.name, SITE_URL + self.event.get_absolute_url())
        for field in self.fields:
            self.fields[field].widget.attrs['ng-model'] = 'form.' + field
            self.fields[field].widget.attrs['ng-Initial'] = 'True'