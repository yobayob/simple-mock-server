# -*- coding: utf-8 -*-
import uuid

from django.db import models
from django.db.models.signals import pre_save, post_save
from django.core.validators import EmailValidator, URLValidator
from django.core.exceptions import ValidationError
from django.core.urlresolvers import reverse
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericRelation
from django.utils.translation import ugettext_lazy as _
from yandex_maps import api
from django.dispatch import receiver
from colorful.fields import RGBColorField
from django.contrib.auth.models import User
from pytils import translit
from os import path
from datetime import date
from family.settings import SITE_URL
from django.conf import settings
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

ORG_STATUS_NEW = 1
ORG_STATUS_APPROVED = 2
ORG_STATUS_BLACKLISTED = 3

STATUS_CHOICES = (
    (ORG_STATUS_NEW, _('New')),
    (ORG_STATUS_APPROVED, _('Approved')),
    (ORG_STATUS_BLACKLISTED, _('Blacklisted')),
)

CONTACT_TYPE_PHONE = 10
CONTACT_TYPE_FAX = 20
CONTACT_TYPE_SITE = 30
CONTACT_TYPE_EMAIL = 40

CONTACT_TYPE_CHOICES = (
    (CONTACT_TYPE_PHONE, _(u'Телефон')),
    (CONTACT_TYPE_FAX, _(u'Факс')),
    (CONTACT_TYPE_SITE, _(u'Сайт')),
    (CONTACT_TYPE_EMAIL, _(u'Электронная почта')),
)


def get_file_path(instance, filename):
    filename = '%s.%s' % (translit.slugify(filename.split('.')[0]), filename.split('.')[-1])
    return path.join(instance.folder, filename)


MALE = 1
FEMALE = 0

SEX_CHOICES = (
    (MALE, _(u'Мужской')),
    (FEMALE, _(u'Женский')),
)


class Patient(models.Model):
    """
    Клиенты
    """
    name = models.CharField(max_length=1000, verbose_name=u"Имя")

    def __unicode__(self):
        return ("%s (ID: %s)") % (self.name, self.id)

    class Meta:
        verbose_name = (u'Клиент')
        verbose_name_plural = (u'Клиенты')


class Passport(models.Model):
    patient = models.ForeignKey(Patient, null=True, blank=True, verbose_name=u'Клиент ID (Если есть в базе)')
    first_name = models.CharField(max_length=1000, verbose_name=u"Имя")
    middle_name = models.CharField(max_length=1000, verbose_name=u"Отчество")
    last_name = models.CharField(max_length=1000, verbose_name=u"Фамилия")
    birth_date = models.DateField(verbose_name=u"Дата рождения")
    sex = models.PositiveIntegerField(choices=SEX_CHOICES, default=MALE, verbose_name=u"Пол")

    address = models.TextField(null=True, blank=True, verbose_name=u'Адрес регистрации')
    fact_address = models.TextField(null=True, blank=True, verbose_name=u'Адрес проживания')

    passport_series = models.IntegerField(verbose_name=u"Серия паспорта")
    passport_number = models.IntegerField(verbose_name=u"Номер паспорта")

    setter_date = models.DateField(verbose_name=u"Дата выдачи паспорта")
    setter_org = models.CharField(max_length=1000, verbose_name=u"Кем выдан паспорт")

    def name(self):
        return u"%s %s %s" % (self.last_name, self.first_name, self.middle_name)

    def age(self):
        today = date.today()
        try:
            age = today.year - self.birth_date.year
            if today.month < self.birth_date.month: age -= 1
            elif today.month == self.birth_date.month and today.day <= self.birth_date.day: age -= 1
            return age
        except:
            return '-'

    def __unicode__(self):
        return ("%s") % (self.name())

    class Meta:
        verbose_name = (u'Клиент')
        verbose_name_plural = (u'Клиенты')


class Contact(models.Model):
    """
    Контакты
    """
    contact_type = models.PositiveIntegerField(choices=CONTACT_TYPE_CHOICES, verbose_name=u"Тип контактной информации")
    contact_value = models.CharField(max_length=1000, verbose_name=u"Значение")
    name = models.CharField(max_length=1000, verbose_name=u"Подробности", blank=True, null=True)
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    def clean(self):
        validator = None
        if self.contact_type == CONTACT_TYPE_SITE:
            validator = URLValidator()
        elif self.contact_type == CONTACT_TYPE_EMAIL:
            validator = EmailValidator()
        if validator:
            validator(self.contact_value)

    def __unicode__(self):
        return self.contact_value

    @property
    def title(self):
        return u'Контакты'

    class Meta:
        verbose_name = (u'Контакт')
        verbose_name_plural = (u'Контакты')


class ContactMixin(models.Model):
    """
    Контакты
    """
    contact = GenericRelation(Contact)

    def get_contact_by_type(self, contact_type):
        r = None
        qs = self.contact.filter(contact_type=contact_type)
        if qs.exists():
            r = qs.first().contact_value
        return r

    @property
    def phone(self):
        return self.get_contact_by_type(CONTACT_TYPE_PHONE)

    @property
    def fax(self):
        return self.get_contact_by_type(CONTACT_TYPE_FAX)

    @property
    def site(self):
        return self.get_contact_by_type(CONTACT_TYPE_SITE)

    @property
    def mail(self):
        return self.get_contact_by_type(CONTACT_TYPE_EMAIL)

    class Meta:
        abstract = True


class District(models.Model):
    """
    Районы
    """
    name = models.CharField(max_length=1000, unique=True, verbose_name=u"Название")

    def __unicode__(self):
        return self.name

    @property
    def title(self):
        return u'Районы'

    class Meta:
        verbose_name = (u'Район')
        verbose_name_plural = (u'Районы')


class Religion(models.Model):
    """
    Конфессия
    """
    name = models.CharField(max_length=1000, unique=True, verbose_name=u"Название")

    def __unicode__(self):
        return self.name

    @property
    def title(self):
        return u'Конфессиональная принадлежность'

    class Meta:
        verbose_name = (u'Конфессиональная принадлежность')
        verbose_name_plural = (u'Конфессиональные принадлежности')


class TypeOrgs(models.Model):
    """
    Типы организаций
    """
    name = models.CharField(max_length=1000, unique=True, verbose_name=u"Название")
    description = models.TextField(null=True, blank=True)
    color = RGBColorField(default="0095B6", verbose_name=u"Цвет метки")

    def __unicode__(self):
        return self.name

    @property
    def title(self):
        return u'Типы организаций'

    class Meta:
        verbose_name = (u'Тип организации')
        verbose_name_plural = (u'Типы организаций')


class LegalTypeOrgs(models.Model):
    """
    Организационно-правовые формы организаций
    """
    name = models.CharField(max_length=1000, unique=True, verbose_name=u"Название")

    def __unicode__(self):
        return self.name

    @property
    def title(self):
        return u'Организационно-правовая форма'

    class Meta:
        verbose_name = (u'Организационно-правовая форма')
        verbose_name_plural = (u'Организационно-правовые формы')


class MapCoorMixin(models.Model):
    coor_x = models.FloatField(null=True, blank=True, verbose_name=u"Координаты X (Не трогать!)")
    coor_y = models.FloatField(null=True, blank=True, verbose_name=u"Координаты У (Не трогать!)")

    @property
    def coor_address(self):
        return self.address

    def get_coor(self):
        pos = api.geocode('', self.coor_address)
        return pos

    def update_coor(self):
        pos = self.get_coor()
        self.coor_y = pos[0]
        self.coor_x = pos[1]
        self.save()

    class Meta:
        abstract = True


class Orgs(ContactMixin, MapCoorMixin):
    """
    Организации
    """
    full_name = models.CharField(max_length=1000, null=True, blank=True, verbose_name=u"Полное название")
    name = models.CharField(max_length=1000, unique=True, verbose_name=u"Название")
    address = models.CharField(max_length=1000, null=True, blank=True, verbose_name=u"Юридический адрес")
    fact_address = models.CharField(max_length=1000, null=True, blank=True, verbose_name=u"Фактический адрес")
    index = models.CharField(max_length=1000, null=True, blank=True, verbose_name=u"Индекс")
    district = models.ForeignKey(District, null=True, blank=True, verbose_name=u"Район")
    type = models.ForeignKey(TypeOrgs, verbose_name=u"Тип организации")
    legal_type = models.ForeignKey(LegalTypeOrgs, verbose_name=u"Организационно-правовая форма", default=1)
    description = models.TextField(null=True, blank=True, verbose_name=u"Описание")
    religion = models.ForeignKey(Religion, null=True, blank=True, verbose_name=u"Конфессиональная принадлежность")
    status = models.IntegerField(choices=STATUS_CHOICES, default=ORG_STATUS_NEW)
    chief = models.CharField(max_length=1000, null=True, blank=True, verbose_name=u"ФИО руководителя")
    chief_post = models.CharField(max_length=1000, null=True, blank=True, verbose_name=u"Должность руководителя")
    uuid = models.UUIDField(primary_key=False, default=uuid.uuid4, editable=False, verbose_name=u"UUID")
    orgn = models.BigIntegerField(unique=True, null=True, blank=True, verbose_name=u"ОГРН")  # ОГРН
    inn = models.BigIntegerField(unique=True, null=True, blank=True, verbose_name=u"ИНН")

    is_in_social_register = models.BooleanField(default=False,
                                                verbose_name=u'Внесены в реестр поставщиков социальных услуг')
    is_certificate_for_patients = models.BooleanField(default=False, verbose_name=u"Обслуживание по сертификатам")
    is_query_certificate_for_patients = models.BooleanField(default=False, verbose_name=u"Подача заявок на сертификаты")

    created = models.DateField(auto_now_add=True, verbose_name=u"Создано")
    changed = models.DateField(auto_now=True, null=True, verbose_name=u"Изменено")

    history = models.TextField(null=True, blank=True, verbose_name=u"История")

    def service_with_seat(self):
        return self.socialservice_set.filter(type__have_seat=True)

    def have_service_with_seat(self):
        return self.service_with_seat().exists()

    def last_updated_blanks(self):
        return self.blanks.all().order_by('-changed')[:10]

    @property
    def coor_address(self):
        a = ''
        if self.fact_address:
            a = self.fact_address
        elif self.address:
            a = self.address
        return a

    def get_absolute_url(self):
        url = reverse('org_detail', kwargs={'pk':self.pk})
        return url

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = (u'Организация')
        verbose_name_plural = (u'Организации')


class RehabProgram(models.Model):
    """
    Реабилитационные программы
    """
    org = models.ForeignKey(Orgs, verbose_name=u"Организация")
    name = models.CharField(max_length=1000, verbose_name=u"Название")
    file = models.FileField(upload_to=get_file_path, blank=True, null=True, verbose_name=u"Файл")

    def __unicode__(self):
        return self.name

    @property
    def title(self):
        return u'Программы комплексной реабилитации и ресоциализации'

    @property
    def folder(self):
        return u'RehabProgram'

    class Meta:
        verbose_name = (u'Программа комплексной реабилитации и ресоциализации')
        verbose_name_plural = (u'Программы комплексной реабилитации и ресоциализации')


class CertificateType(models.Model):
    """
    Типы сертификатов
    """
    name = models.CharField(max_length=1000, unique=True, verbose_name=u"Название")

    def __unicode__(self):
        return self.name

    @property
    def title(self):
        return u'Типы сертификатов'

    class Meta:
        verbose_name = (u'Тип сертификата')
        verbose_name_plural = (u'Типы сертификатов')


class Certificate(models.Model):
    """
    Сертификаты (только для организации)
    """
    type = models.ForeignKey(CertificateType, verbose_name=u"Тип сертификата")
    number = models.CharField(max_length=1000, null=True, blank=True, verbose_name=u"Номер")  # Номер
    org = models.ForeignKey(Orgs, verbose_name=u"Организация")
    setter_org = models.CharField(max_length=1000, null=True,
                                  verbose_name=u"Организация, выдавшая сертификат")  # Организация, выдавшая сертификат
    setter_date = models.DateField(null=True, blank=True, verbose_name=u"Дата выдачи")
    address = models.TextField(null=True, blank=True, verbose_name=u"Адреса действия")  # по строке на адрес

    created = models.DateField(auto_now_add=True, verbose_name=u"Создано")
    changed = models.DateField(auto_now=True, verbose_name=u"Изменено")

    def __unicode__(self):
        return '%s - %s' % (self.org.name, self.type.name)

    class Meta:
        verbose_name = (u'Сертификат')
        verbose_name_plural = (u'Cертификаты соответствия')


class LicenseType(models.Model):
    """
    Типы лицензий
    """
    name = models.CharField(max_length=1000, unique=True, verbose_name=u"Название")

    def __unicode__(self):
        return self.name

    @property
    def title(self):
        return u'Типы лицензий'

    class Meta:
        verbose_name = (u'Тип лицензии')
        verbose_name_plural = (u'Типы лицензий')


class License(models.Model):
    """
    Лицензии
    """
    type = models.ForeignKey(LicenseType, verbose_name=u"Тип лицензии")
    number = models.CharField(max_length=1000, null=True, blank=True, verbose_name=u"Номер лицензии")  # Номер
    org = models.ForeignKey(Orgs, verbose_name=u"Организация")
    setter_org = models.CharField(max_length=1000, null=True,
                                  verbose_name=u"Организация, выдавшая сертификат")  # Организация, выдавшая лицензию
    setter_date = models.DateField(null=True, blank=True, verbose_name=u"Дата выдачи")
    address = models.TextField(null=True, blank=True, verbose_name=u"Адреса действия")  # по строке на адрес

    created = models.DateField(auto_now_add=True, verbose_name=u"Дата создания")
    changed = models.DateField(auto_now=True, verbose_name=u"Дата последнего изменения")

    def __unicode__(self):
        return '%s - %s' % (self.org.name, self.type.name)

    class Meta:
        verbose_name = (u'Лицензия')
        verbose_name_plural = (u'Лицензии')


class Legislation(models.Model):
    """
    Законодательство
    """
    name = models.CharField(max_length=1000, verbose_name=u"Наименование нормативно-правового акта")
    date = models.DateField(verbose_name=u"Дата принятия")
    file = models.FileField(upload_to=get_file_path, verbose_name="файл")

    @property
    def folder(self):
        return u'Legislation'

    def __unicode__(self):
        return '%s - %s' % (self.date, self.name)

    def extension(self):
        name, extension = path.splitext(self.file.name)
        return extension

    class Meta:
        verbose_name = (u'Нормативно-правовой акт')
        verbose_name_plural = (u'Нормативно-правовые акты')


class Event(models.Model):
    """
    Календарь мероприятий
    """
    date = models.DateTimeField(verbose_name=u"Дата проведения")
    name = models.CharField(max_length=1000, verbose_name=u"Название мероприятия")
    organization = models.ForeignKey(Orgs)
    address = models.TextField(verbose_name=u"Место проведения")
    participant = models.TextField(verbose_name=u"Категория участников")
    description = models.TextField(null=True, blank=True, verbose_name=u"Дополнительная информация")

    created = models.DateField(auto_now_add=True, verbose_name=u"Дата создания")
    changed = models.DateField(auto_now=True, verbose_name=u"Дата последнего изменения")

    def get_absolute_url(self):
        url = reverse('event_detail', kwargs={'pk': self.pk})
        return url

    def __unicode__(self):
        return '%s. %s (%s)' % (self.date, self.name, self.organization.name)

    class Meta:
        verbose_name = (u'Мероприятие')
        verbose_name_plural = (u'Мероприятия')


class SocialServiceType(models.Model):
    """
    Типы социальных служб
    """
    name = models.CharField(max_length=1000, unique=True, verbose_name=u"Название")
    description = models.TextField(null=True, blank=True, verbose_name=u"Описание")
    have_seat = models.BooleanField(default=True,
                                    verbose_name=u'Есть возможность указывать информацию о свободных местах')

    def __unicode__(self):
        return self.name

    @property
    def title(self):
        return u'Типы подразделений'

    class Meta:
        verbose_name = (u'Типы подразделений')
        verbose_name_plural = (u'Типы подразделений')


class SocialServiceTargetGroup(models.Model):
    """
    Целевые групы
    """
    name = models.CharField(max_length=1000, unique=True, verbose_name=u"Название")

    def __unicode__(self):
        return self.name

    @property
    def title(self):
        return u'Целевая группа'

    class Meta:
        verbose_name = (u'Целевая группа')
        verbose_name_plural = (u'Целевые группы')


class SpecialistType(models.Model):
    """ Специалисты """ 
    name = models.CharField(max_length=1000, verbose_name=u"Имя специалиста", unique=True)

    def __unicode__(self):
        return self.name

    @property
    def title(self):
        return u'Специалист'

    class Meta:
        verbose_name = (u'Специалист')
        verbose_name_plural = (u'Специалисты')


class SocialServiceBase(ContactMixin):
    """ Тело соц служб """ 
    name = models.CharField(max_length=1000, unique=True, verbose_name=u"Название")
    type = models.ForeignKey(SocialServiceType, null=True, verbose_name=u"Тип подразделения")
    org = models.ForeignKey(Orgs, verbose_name=u"Организация")
    description = models.TextField(null=True, blank=True, verbose_name=u"Описание")
    address = models.CharField(max_length=1000, null=True, blank=True, verbose_name=u"Адрес")
    target_group = models.ManyToManyField(SocialServiceTargetGroup, blank=True, verbose_name=u'Целевая группа')

    have_religion_content = models.BooleanField(default=False, verbose_name=u'Наличие религиозного содержания')
    have_accessible_env = models.BooleanField(default=False, verbose_name=u'Наличие доступной среды')

    created = models.DateField(auto_now_add=True)
    changed = models.DateField(auto_now=True)

    chief = models.CharField(max_length=1000, null=True, blank=True, verbose_name=u"ФИО руководителя подразделения")
    chief_post = models.CharField(max_length=1000, null=True, blank=True,
                                  verbose_name=u"Должность руководителя подразделения")

    def get_site_name(self):
        if self.site:
            return self.site.replace('http://', '')[0:40]

    @classmethod
    def get_approved(cls):
        return cls.objects.filter(org__status=ORG_STATUS_APPROVED)

    class Meta:
        abstract = True


class SocialService(SocialServiceBase, MapCoorMixin):
    """ Социальные службы """
    specialist = models.ManyToManyField(SpecialistType, verbose_name=u'Специалисты', blank=True)

    seats = models.IntegerField(null=True, blank=True, verbose_name=u"Всего мест")
    seats_for_men = models.IntegerField(null=True, blank=True, verbose_name=u"Всего мест для мужчин")
    seats_for_woman = models.IntegerField(null=True, blank=True, verbose_name=u"Всего мест для женщин")

    def clean(self):
        if self.type and not self.type.have_seat:
            if any((self.seats, self.seats_for_men, self.seats_for_woman)):
                raise ValidationError(_('Seat not allowed for this type'))

    def last_seats(self):
        try:
            r = Seat.objects.filter(social_service=self).order_by('id').last()
        except Seat.DoesNotExist:
            r = None
        return r

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        url = reverse('social_service_detail', kwargs={'pk':self.pk})
        return url

    class Meta:
        verbose_name = (u'Подразделение')
        verbose_name_plural = (u'Подразделения')


CERTIFICATE_STATUS_REQUESTED = 10
CERTIFICATE_STATUS_APPROVED = 20
CERTIFICATE_STATUS_REJECTED = 30
CERTIFICATE_STATUS_COMPLETED = 40

CERTIFICATE_STATUS = (
    (CERTIFICATE_STATUS_REQUESTED, _(u'Запрошен')),
    (CERTIFICATE_STATUS_APPROVED, _(u'Одобрен')),
    (CERTIFICATE_STATUS_REJECTED, _(u'Отклонен')),
    (CERTIFICATE_STATUS_COMPLETED, _(u'Выполнен')),
)


class CertificateForPatients(models.Model):
    """
    Сертификаты на оказание услуг (для паицентов)
    """
    patient = models.ForeignKey(Passport, verbose_name=u"Клиент")
    social_service = models.ForeignKey(SocialService, verbose_name=u"Место направления")
    setter_org = models.ForeignKey(Orgs, null=True, blank=True, verbose_name=u'Направлен из')
    date_start = models.DateField(null=True, verbose_name=u"Дата начала")
    date_end = models.DateField(null=True, verbose_name=u"Дата истечения")
    uuid = models.UUIDField(primary_key=False, default=uuid.uuid4, editable=False, verbose_name=u"UUID")
    status = models.IntegerField(choices=CERTIFICATE_STATUS, default=CERTIFICATE_STATUS_REQUESTED, verbose_name=u"Статус")

    created = models.DateField(auto_now_add=True, null=True)
    changed = models.DateField(auto_now=True, null=True)

    def get_steps(self):
        return CertificateForPatientsStep.objects.filter(certificate=self).order_by('step')

    def step(self):
        steps = CertificateForPatientsStep.objects.filter(certificate=self).order_by('step')
        for step in steps:
            if not step.status:
                return step
        return steps[3]

    def __unicode__(self):
        return u'СР-%s %s направлен в %s' % (self.id, self.patient.name(), self.social_service.name)

    def get_absolute_url(self):
        url = reverse('certificate_detail', kwargs={'pk': self.pk})
        return url

    def get_full_url(self):
        return ("%s%s") % (SITE_URL, self.get_absolute_url())

    class Meta:
        verbose_name = (u'Сертификат на оказание услуг')
        verbose_name_plural = (u'Cертификаты на оказание услуг')

CERT_STEP_1 = 1

STATUS_CERTIFICATE = (
    (None, _(u'Выдан')),
    (CERT_STEP_1, _(u'Погашен')),
)


STEP_1 = 1
STEP_2 = 2
STEP_3 = 3
STEP_4 = 4

STEP = (
    (None, _(u'Нет информации')),
    (STEP_1, _(u'Отметка о начала прохождения курса социальной реабилитации')),
    (STEP_2, _(u'Отметка о завершении курса социальной реабилитации')),
    (STEP_3, _(u'Отметка о начале постреабилитационного периода')),
    (STEP_4, _(u'Отметка о завершении постреабилитационного периода'))
)


class CertificateForPatientsStep(models.Model):
    """
    Купоны сертификатов
    """
    certificate = models.ForeignKey(CertificateForPatients, verbose_name=u"Сертификат")
    status = models.IntegerField(choices=STATUS_CERTIFICATE, null=True, default=None, verbose_name=u"Статус")
    step = models.IntegerField(choices=STEP, null=False, default=STEP_1)
    date_start = models.DateField(null=True, verbose_name=u"Дата начала")
    date_end = models.DateField(null=True, verbose_name=u"Дата истечения")

    created = models.DateField(auto_now_add=True, null=True)
    changed = models.DateField(auto_now=True, null=True)

    def save(self, **kwargs):
        super(CertificateForPatientsStep, self).save(**kwargs)
        if self.step == STEP_4 and self.status == CERT_STEP_1:
            self.certificate.status = CERTIFICATE_STATUS_COMPLETED
            self.certificate.save()

    def code(self):
        return str(self.id).zfill(7)

    def can_close(self):
        if self.certificate.status != CERTIFICATE_STATUS_APPROVED: return False 
        if self.status: return False #Статус есть, значит уже погашен или просрочен
        if self.step == STEP_1: return True #Этап 1 - можно гасить
        previous_step = CertificateForPatientsStep.objects.get(certificate=self.certificate, step=self.step-1)
        if previous_step.status == CERT_STEP_1: return True #Предыдущий статус погашен
        else: return False

    def get_full_close_url(self):
        return (u"%s%s") % (SITE_URL, self.get_close_url())

    def get_close_url(self):
        url = reverse('step_close', kwargs={'pk': self.pk})
        return url

    def __unicode__(self):
        return u'СР-%s шаг %s %s (%s)' % (self.certificate.id, self.step, self.code(), self.get_status_display())

    class Meta:
        verbose_name = (u'Купон сертификата')
        verbose_name_plural = (u'Купон сертификата')


class FormProvisionService(models.Model):
    """
    Формы оказания услуг
    """
    name = models.CharField(max_length=1000, verbose_name=u"Название", unique=True)

    def __unicode__(self):
        return self.name

    @property
    def title(self):
        return u'Форма оказания услуги'

    class Meta:
        verbose_name = (u'Форма оказания услуги')
        verbose_name_plural = (u'Формы оказания услуг')


class SocialServiceItem(models.Model):
    """
    Услуги оказываемые в реабилитационных центрах
    """
    name = models.CharField(max_length=1000, verbose_name=u"Название")
    indications = models.TextField(null=True, blank=True, verbose_name=u'Показания к назначению')
    requirements = models.TextField(null=True, blank=True, verbose_name=u'Требования к клиенту')
    term_of_service = models.CharField(max_length=1000, null=True, blank=True, verbose_name=u'Срок оказания услуги')
    form_of_provision = models.ForeignKey(FormProvisionService, verbose_name=u'Форма оказания услуги')
    cost = models.BigIntegerField(verbose_name=u'Стоимость (0 если бесплатно)', default=0)
    description = models.TextField(null=True, blank=True, verbose_name=u'Дополнительная информация')
    social_service = models.ForeignKey(SocialService, verbose_name=u'Подразделение')

    def __unicode__(self):
        return (u'%s в %s - %dр') % (self.name, self.social_service.name, self.cost)

    @property
    def title(self):
        return u'Услуга'

    class Meta:
        verbose_name = (u'Услуга')
        verbose_name_plural = (u'Услуги')


class Seat(models.Model):
    """ Места в реабилитационных центрах """
    social_service = models.ForeignKey(SocialService, verbose_name=u"Подразделение")
    seats = models.IntegerField(null=True, blank=True, verbose_name=u"Общее количество мест")
    seats_for_men = models.IntegerField(null=True, blank=True, verbose_name=u"Места для мужчин")
    seats_for_woman = models.IntegerField(null=True, blank=True, verbose_name=u"Места для женщин")
    created = models.DateField(auto_now_add=True, verbose_name=u"Дата создания")

    def clean(self):
        if not self.social_service.type.have_seat:
            raise ValidationError(
                u'Нельзя указать информацию о свободных местах для подразделения типа %s' % self.social_service.type.name
            )

    def __unicode__(self):
        return self.social_service.name

    class Meta:
        verbose_name = (u'Места в реабилитационных центрах')
        verbose_name_plural = (u'Места в реабилитационных центрах')


class MS(SocialServiceBase):
    """ Мобильная служба """
    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = (u'Мобильная служба')
        verbose_name_plural = (u'Мобильные службы')



EDUCATION_CHOICES = (
    (0, u'Среднее'),
    (1, u'Высшее'),
    (2, u'Незаконченное высшее')
)

JOB_CHOICES = (
    (0, u'Работающий'),
    (1, u'Не работающий'),
    (2, u'Зарегистрирован как безработный')
)


class Blank(models.Model):
    """
    Специалист оказывает услуги основываясь на учетной карте.
    """
    patient = models.ForeignKey(Passport,
                                        verbose_name=u"Клиент")
    organization = models.ForeignKey(Orgs, related_name='blanks',
                                        verbose_name=u'Организация')
    reason_for_request = models.TextField(blank=True, null=True,
                                        verbose_name=u'Цель обращения')
    phone = models.CharField(verbose_name=u"Телефон",
                                        max_length=1000)
    citizenship = models.CharField(verbose_name=u"Гражданство",
                                        max_length=1000)
    category_of_client = models.CharField(max_length=1000,
                                        verbose_name=u'Категория заявителя')
    education = models.PositiveIntegerField(choices=EDUCATION_CHOICES,
                                        verbose_name=u'Образование')
    position = models.CharField(verbose_name=u"Основная профессия",
                                        max_length=1000)
    job = models.PositiveIntegerField(choices=JOB_CHOICES,
                                        verbose_name=u'Место работы')
    sources_of_income = models.CharField(verbose_name=u"Источник дохода",
                                        max_length=1000)
    per_capita_income = models.CharField(verbose_name=u"Среднедушевой доход",
                                        max_length=1000)
    nark = models.BooleanField(default=False,
                                        verbose_name=u'Наличие официального документа, '
                                                     u'подтверждающего диагноз «Наркомания»')
    file = models.FileField(upload_to=get_file_path, null=True, blank=True,
                            verbose_name=u"Результаты опроса получателя социальных услуг "
                                         u"по методике «Индекс тяжести зависимости» (файл)")

    comment = models.TextField(null=True, blank=True,
                               verbose_name=u'Комментарий')

    created = models.DateField(auto_now_add=True, null=True, verbose_name=u"Создано")
    changed = models.DateField(auto_now=True, null=True, verbose_name=u"Изменено")

    @property
    def folder(self):
        return u'Blanks'

    def __unicode__(self):
        return u'Учетная карта #%d' % self.pk

    def get_absolute_url(self):
        return reverse('blank_detail', kwargs={'pk':self.pk})

    class Meta:
        verbose_name = u'Учетная карточка'
        verbose_name_plural = u'Учетные карточки'



class BlankServiceItem(models.Model):
    name = models.CharField(max_length=1000, verbose_name=u'Наименование услуги')
    form_of_provision = models.ForeignKey(FormProvisionService, verbose_name=u'Форма оказания услуги')
    description = models.TextField(null=True, blank=True, verbose_name=u'Дополнительная информация')
    organization = models.ForeignKey(Orgs, related_name='blank_services',
                                     verbose_name=u'Организация')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'Услуга, оказываемая специалистом'
        verbose_name_plural = u'Услуги, оказываемые специалистами'


STATUS_PLAN_NONE = 0
STATUS_PLAN_YES = 1
STATUS_PLAN_CANCEL = 2

STATUS_PLAN_CHOICES = (
    (0, u'Услуга не оказана'),
    (1, u'Услуга оказана'),
    (2, u'Услуга отменена')
)


class BlankServicePlan(models.Model):
    """
    План получения услуг
    """
    blank = models.ForeignKey(Blank, verbose_name=u'Учетная карта')
    service = models.ForeignKey(BlankServiceItem, verbose_name=u'Услуга')
    date_start = models.DateField(verbose_name=u'Дата начала обслуживания')
    date_end = models.DateField(verbose_name=u'Дата окончания обслуживания')
    user = models.ForeignKey(User, verbose_name=u'Специалист',
                             related_name='blank_services')

    def __unicode__(self):
        return '%s - %s' % (self.blank.patient.name(), self.service.name)

    class Meta:
        verbose_name = u'Услуга из плана обслуживания клиентов'
        verbose_name_plural = u'План обслуживания клиентов'


class BlankService(models.Model):
    """
    Факт получения соц. услуги
    """

    service_plan = models.ForeignKey(BlankServicePlan,
                                        null=True, verbose_name=u'Услуга')
    date = models.DateField(verbose_name=u'Дата услуги',
                                        default=date.today())
    place = models.CharField(verbose_name=u'Место проведения услуги',
                                        max_length=1000)
    file = models.FileField(upload_to=get_file_path,
                                        blank=True, null=True,
                                        verbose_name=u"Результаты анкетирования")
    status = models.PositiveIntegerField(choices=STATUS_PLAN_CHOICES,
                                         default=STATUS_PLAN_YES,
                                         verbose_name=u'Статус услуги')

    cancelled_date = models.DateField(verbose_name=u'Дата отмены услуги',
                                        blank=True, null=True)
    cancelled_reason = models.CharField(blank=True, null=True, max_length=1000,
                                        verbose_name=u'Причина отмены')

    created = models.DateField(auto_now_add=True,
                                        verbose_name=u"Создано")
    changed = models.DateField(auto_now=True,
                                        null=True, verbose_name=u"Изменено")

    @property
    def folder(self):
        return u'BlankService'

    class Meta:
        verbose_name = u'Факт получения социальных услуг'
        verbose_name_plural = u'Социальные услуги'

    def __unicode__(self):
        return self.service_plan.service.name


class FamilyMember(models.Model):
    """
    Член семьи получателя соц. услуг
    """
    blank = models.ForeignKey(Blank, related_name='family_members',
                                verbose_name=u'Учетная карточка пациента')
    full_name = models.CharField(max_length=1000, verbose_name=u'Полное имя')
    birthdate = models.DateField(verbose_name=u'Дата рождения')
    capacity = models.BooleanField(default=False,
                                verbose_name=u'Дееспособность')
    earning_capacity = models.BooleanField(default=False,
                                verbose_name=u'Трудоспособность')
    relation_degree = models.CharField(max_length=1000,
                                verbose_name=u'Степень родства')
    income = models.CharField(verbose_name=u"Доход",
                                max_length=1000)
    registration = models.BooleanField(default=False,
                                verbose_name=u'Наличие регистрации по адресу заявителя')

    class Meta:
        verbose_name = u'Член семьи'
        verbose_name_plural = u'Члены семьи'




CONS_STATUS_APPEAL = 1
CONS_STATUS_APPEAL_ANOTHER = 2
CONS_STATUS_CANCELLED = 3

STATUS_CONSULTATION = (
    (None, _(u'Нет информации')),
    (CONS_STATUS_APPEAL, _(u'Обратился')),
    (CONS_STATUS_APPEAL_ANOTHER, _(u'Обратился в другую организацию')),
    (CONS_STATUS_CANCELLED, _(u'Отменено'))
)



class Consultation(models.Model):
    """
    Журнал учета консультаций
    """
    id_in_organization = models.PositiveIntegerField(null=True, blank=True, verbose_name=u"Порядковый номер консультации в организации")
    patient = models.ForeignKey(Patient, null=True, blank=True, verbose_name=u"Клиент")
    primary_treatment = models.BooleanField(default=False, verbose_name=u"Первичное обращение с проблемой")
    primary_treatment_org = models.BooleanField(default=False, verbose_name=u"Первичное обращение в организацию")
    specialist = models.TextField(null=True, verbose_name=u"Сведения о специалистах")
    organization = models.ForeignKey(Orgs, verbose_name=u"Организация")
    date = models.DateField(null=True, verbose_name=u"Дата консультации")
    treatment = models.TextField(null=True, blank=True, verbose_name=u'Краткое описание содержания обращения')
    result_info = models.TextField(null=True, blank=True, verbose_name=u'Краткое описание результатов консультации')
    description = models.TextField(null=True, blank=True, verbose_name=u'Дополнительная информация')
    from_social_service = models.ForeignKey(SocialService, null=True, blank=True, verbose_name=u"Направлен из")
    from_social_service_text = models.CharField(max_length=1000, null=True, blank=True, verbose_name=u"Направлен из")
    sent_to_text = models.CharField(max_length=1000, null=True, blank=True, verbose_name=u"Направлен в")

    """
    Контактные данные клиента, находятся здесь, так как они могут меняться чаще чем паспорт
    """
    phone = models.CharField(max_length=1000, null=True, blank=True, verbose_name=u"Телефон")
    email = models.CharField(max_length=1000, null=True, blank=True, verbose_name=u"Электронная почта")

    """
    Предоставленная клиентом дполнительная информация о себе
    """
    additional_info_1 = models.BooleanField(default=False, verbose_name=u"О наличии вакансий/порядке обращения в службу занятости")
    additional_info_2 = models.BooleanField(default=False, verbose_name=u"О порядке предоставления помощи ВИЧ-инфицированным")
    additional_info_3 = models.BooleanField(default=False, verbose_name=u"О режиме и порядке работы групп взаимопомощи")
    additional_info_4 = models.BooleanField(default=False, verbose_name=u"О порядке получения услуг по социальной реабилитации и ресоциализации")
    additional_info_5 = models.BooleanField(default=False, verbose_name=u"О порядке получения социальных услуг")
    additional_info_6 = models.BooleanField(default=False, verbose_name=u"О порядке получения медицинской помощи")
    additional_info_7 = models.BooleanField(default=False, verbose_name=u"О службах занятости населения")
    additional_info_8 = models.BooleanField(default=False, verbose_name=u"О СПИД-центрах")
    additional_info_9 = models.BooleanField(default=False, verbose_name=u"О группах взаимопомощи")
    additional_info_10 = models.BooleanField(default=False, verbose_name=u"О реабилитационных центрах для лиц, отказавшихся от немедицинского потребления наркотиков")
    additional_info_11 = models.BooleanField(default=False, verbose_name=u"О государственных учреждениях-поставщиках социальных услуг")
    additional_info_12 = models.BooleanField(default=False, verbose_name=u"О медицинских учреждениях наркологического профиля")

    """
    Рекомендованные специалисты
    """
    specialist_1 = models.BooleanField(default=False, verbose_name=u"Психологу")
    specialist_2 = models.BooleanField(default=False, verbose_name=u"Юристу")
    specialist_3 = models.BooleanField(default=False, verbose_name=u"Врачу-наркологу")
    specialist_4 = models.BooleanField(default=False, verbose_name=u"Педагогу")
    specialist_5 = models.BooleanField(default=False, verbose_name=u"Врачу-иммунологу")
    specialist_6 = models.BooleanField(default=False, verbose_name=u"Специалисту по работе с семьей")
    specialist_7 = models.BooleanField(default=False, verbose_name=u"Психотерапевту")
    specialist_8 = models.BooleanField(default=False, verbose_name=u"Специалисту по социальной работе")
    specialist_text = models.CharField(max_length=1000, null=True, blank=True, verbose_name=u"Другие специалисты")

    created = models.DateField(auto_now_add=True, null=True)
    changed = models.DateField(auto_now=True, null=True)

    def sent_to(self):
        return Direction.objects.filter(consultation=self)

    def __unicode__(self):
        return ('%s - %s') % (self.date, self.patient.name)

    def sent(self):
        answer = []
        if self.sent_to().exists():
            answer = [i.social_service.name for i in self.sent_to()]
        if self.sent_to_text: answer.append(self.sent_to_text)
        return answer

    def get_absolute_url(self):
        url = reverse('consultation_detail', kwargs={'pk': self.pk})
        return url

    def get_full_url(self):
        return ("http://%s%s") % (SITE_URL, self.get_absolute_url())

    class Meta:
        verbose_name = (u'Консультация')
        verbose_name_plural = (u'Консультации')


class Direction(models.Model):
    """
    Направление после консультации
    """

    consultation = models.ForeignKey(Consultation, verbose_name=u"Консультация")
    social_service = models.ForeignKey(SocialService, verbose_name=u"Направлен в")
    status = models.IntegerField(choices=STATUS_CONSULTATION, null=True, default=None, verbose_name=u"Статус")

    def __unicode__(self):
        return (u'Консультация №%d, направление в %s') % (self.consultation.pk, self.social_service.name)

    class Meta:
        verbose_name = (u'Направление на консультацию')
        verbose_name_plural = (u'Направления на консультацию')


class RouteMS(MapCoorMixin):
    """
    Маршрут мобильной службы
    """

    time = models.CharField(max_length=1000, verbose_name=u"Время")
    ms = models.ForeignKey(MS, verbose_name=u"Мобильная служба")
    address = models.CharField(max_length=1000, null=True, blank=True, verbose_name=u"Адрес")
    description = models.TextField(null=True, blank=True, verbose_name=u"Описание")

    def __unicode__(self):
        return '%s - %s' % (self.ms.name, self.time)

    class Meta:
        verbose_name = (u'Нахождение мобильной службы')
        verbose_name_plural = (u'Маршрут мобильной службы')


class Profile(ContactMixin, models.Model):
    """
    Профиль
    """
    user = models.OneToOneField(User)
    organization = models.ForeignKey(Orgs, blank=True,
                                            null=True)
    position = models.CharField(null=True, blank=True, max_length=1000,
                                            verbose_name=u"Должность")
    time_work = models.TextField(null=True, blank=True, default=u"10:00 - 18:00",
                                            verbose_name=u"Время работы")
    specialization = models.TextField(null=True, blank=True,
                                            verbose_name=u"Специализация")
    notification_event = models.BooleanField(default=True,
                                            verbose_name=u"Оповещения о новых мероприятиях")
    avatar = models.ImageField(null=True, blank=True, upload_to=get_file_path,
                                            verbose_name=u'Аватар')

    avatar_sm = ImageSpecField( source='avatar',
                                   processors=[ResizeToFill(200, 200)],
                                   format='JPEG',
                                   options={'quality': 90})

    created = models.DateField(auto_now_add=True, null=True)
    changed = models.DateField(auto_now=True, null=True)

    def get_mugshot_url(self):
        if self.avatar:
            try:
                return self.avatar_sm.url
            except IOError:
                pass
        return settings.DEFAULT_USER_PIC

    @property
    def folder(self):
        return u'Profile'

    def __unicode__(self):
        return '%s' % (self.user.get_full_name())

    def get_absolute_url(self):
        return reverse('user_profile', kwargs={'pk':self.pk})

    class Meta:
        verbose_name = (u'Профили')
        verbose_name_plural = (u'Профиль')


def get_username(self):
    """
    Monkey patch to user name:
    """
    try:
        return self.profile.__unicode__()
    except AttributeError:
        return self.username

User.__unicode__ = lambda self: get_username(self)




def get_coordinates(sender, instance, **kwargs):
    pos = instance.get_coor()
    instance.coor_y = pos[0]
    instance.coor_x = pos[1]


pre_save.connect(get_coordinates, sender=Orgs)
pre_save.connect(get_coordinates, sender=RouteMS)
pre_save.connect(get_coordinates, sender=SocialService)


@receiver(post_save, sender=User)
def create_profile(sender, instance, created=False, **kwargs):
    if created:
        if not User.objects.get(pk=instance.pk):
            Profile.objects.create(user=instance)
    return instance

@receiver(pre_save, sender=Consultation)
def set_organization_id(sender, instance, **kwargs):
    if instance._state.adding is True:
        if not Consultation.objects.filter(organization=instance.organization).exists():
            instance.id_in_organization = 1
        else:
            instance.id_in_organization = Consultation.objects.latest('id').id_in_organization + 1

@receiver(post_save, sender=CertificateForPatients)
def create_certificate_for_patients(sender, instance, created=False, **kwargs):
    if created:
        for i in range(1,5):
            CertificateForPatientsStep.objects.create(certificate=instance, step=i, status=None)
    return instance