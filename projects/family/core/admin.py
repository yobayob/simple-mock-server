# -*- coding: utf-8 -*-
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.contenttypes.admin import GenericStackedInline
from django.utils.translation import ugettext_lazy as _
from easy_select2 import select2_modelform
from django.forms import *
from models import *
from django.contrib.auth.models import User
from core.tasks import send_mail_task

SocialServiceForm = select2_modelform(SocialService, attrs={'width': '250px'})


class MapAdminMixin(object):
    exclude = ('coor_x', 'coor_y')


class SocialServiceAdminInline(MapAdminMixin, admin.StackedInline):
    model = SocialService
    form = SocialServiceForm
    extra = 1


class RouteMSInline(MapAdminMixin, admin.StackedInline):
    model = RouteMS
    extra = 1


class MSAdminInline(admin.StackedInline):
    model = MS
    extra = 1


class ContactAdminInline(GenericStackedInline):
    model = Contact
    extra = 1


class LicenseAdminInline(admin.StackedInline):
    model = License
    extra = 1


class CertificateAdminInline(admin.StackedInline):
    model = Certificate
    extra = 1


class RehabProgramAdminInline(admin.StackedInline):
    model = RehabProgram
    extra = 1


class SocialServiceItemAdminInline(admin.StackedInline):
    model = SocialServiceItem
    extra = 1


def make_approved(modeladmin, request, queryset):
    queryset.update(status=ORG_STATUS_APPROVED)


make_approved.short_description = _("Mark selected stories as approved")


class OrgsAdmin(MapAdminMixin, admin.ModelAdmin):
    inlines = (
        ContactAdminInline,
        RehabProgramAdminInline,
        CertificateAdminInline,
        LicenseAdminInline,
        SocialServiceAdminInline,
        MSAdminInline
    )
    list_filter = ('status', 'district')
    list_display = ('name', 'status', 'type', 'district', 'inn', 'orgn', 'phone', 'fax', 'site', 'mail')
    search_fields = ('name', 'type__name', 'district__name', 'inn', 'orgn', 'contact__contact_value')
    actions = [make_approved]


class MSAdmin(admin.ModelAdmin):
    inlines = (ContactAdminInline, RouteMSInline,)


class SeatAdminInline(admin.StackedInline):
    model = Seat
    extra = 1


class SocialServiceAdmin(MapAdminMixin, admin.ModelAdmin):
    form = SocialServiceForm
    inlines = (ContactAdminInline, SeatAdminInline, SocialServiceItemAdminInline)
    list_display = ('name','org','type', 'address')


class UserProfileAdmin(admin.StackedInline):
    model = Profile


class AuthUserCreationForm(ModelForm):

    error_messages = {
        'duplicate_username': u'Пользователь с таким никнеймом уже существует',
    }

    class Meta:
        model = User
        fields = '__all__'

    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            User._default_manager.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError(self.error_messages['duplicate_username'])

    def save(self, commit=True):
        user = super(AuthUserCreationForm, self).save(commit=False)
        password = User.objects.make_random_password()
        user.set_password(password)
        if commit:
            user.save()
        head = u'Регистрация в электронной системе перенаправления клиентов'
        text = u'''Здравствуйте, уважаемый пользователь!\n
Вы получили доступ к «Электронной системе перенаправления клиентов регионального сегмента комплексной реабилитации лиц с наркотической зависимостью Санкт-Петербурга»:  https://srnzspb.ru/\n
Для того, чтобы начать работу, Вам необходимо авторизироваться.\n\n
Имя пользователя: %s\n
Ваш пароль: %s\n\n
Вашей организации в системе уже создан Профиль.\n
Просим Вас дополнить свой профиль,  внести в него изменения, если сведения устарели или имеются неточности.  Своевременно вносите информацию о предоставляемых Вами услугах и обслуженных клиентах.
При возникновении вопросов или затруднений, обращайтесь в «Учебно-методический отдел по социальной реабилитации и ресоциализации лиц с зависисмым и созависимым поведением», по телефону: 8-812-417-31-51\n\n
Методист: Смирнова Анастасия Алексеевна.\n
Будем Вам признательны, если Вы пришлете нам отзыв о работе в системе.
    ''' % (user.username, password)
        send_mail_task.delay(head, text, [user.email])
        return user


class MyUserAdmin(UserAdmin):
    add_form = AuthUserCreationForm
    inlines = (UserProfileAdmin,)

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email'),
        }),
    )


class FamilyMemberAdmin(admin.StackedInline):
    model = FamilyMember
    extra = 1

class BlankAdmin(admin.ModelAdmin):
    inlines = (FamilyMemberAdmin,)



admin.site.register(District)
admin.site.register(TypeOrgs)
admin.site.register(Orgs, OrgsAdmin)
admin.site.register(Religion)
admin.site.register(SocialServiceType)
admin.site.register(SocialServiceItem)
admin.site.register(Certificate)
admin.site.register(CertificateForPatients)
admin.site.register(CertificateForPatientsStep)
admin.site.register(CertificateType)
admin.site.register(License)
admin.site.register(Passport)
admin.site.register(LicenseType)
admin.site.register(SpecialistType)
admin.site.register(FormProvisionService)
admin.site.register(SocialServiceTargetGroup)
admin.site.register(MS, MSAdmin)
admin.site.register(SocialService, SocialServiceAdmin)
admin.site.register(LegalTypeOrgs)
admin.site.register(Legislation)
admin.site.unregister(User)
admin.site.register(Event)
admin.site.register(Patient)
admin.site.register(Consultation)
admin.site.register(Blank, BlankAdmin)
admin.site.register(User, MyUserAdmin)
