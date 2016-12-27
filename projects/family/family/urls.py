# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from django_messages.views import compose
from django.contrib.sitemaps.views import sitemap
from core.sitemap import map
from core.models import *
from core import views, wizards
from core.forms import ComposeForm
from public import views as public_views


urlpatterns = patterns(
    '',
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': map, }, name='django.contrib.sitemaps.views.sitemap'),
    url(r'^robots\.txt$', lambda r: views.HttpResponse("User-agent: *\nDisallow: /")),
    url(r'^messages/compose/$', login_required(views.ComposeMessage.as_view()), name='messages_compose'),
    url(r'^messages/compose/(?P<pk>[\d.@+-]+)/$', login_required(views.ComposeMessage.as_view()), name='messages_compose_to'),
    (r'^messages/', include('django_messages.urls')),
)



urlpatterns += patterns(
    '',
    url(r'^$', public_views.IndexView.as_view(), name='start_page'),   # DONE
    url(r'^home/$', public_views.HomeView.as_view(), name='home'),   # DONE
    url(r'^map/$', public_views.MapView.as_view(), name='map'),   # DONE
    url(r'^form/$', views.JoinFormView.as_view(), name='form'),   # DONE
    url(r'^form/success/$', views.JoinFormView.as_view(), kwargs={'success': True}, name='form_success'),   # DONE
    url(r'^login/$', views.LoginView.as_view(), name='login'),   # DONE
    url(r'^add/social_service/$', login_required(views.AddSocialServiceView.as_view()), kwargs={'template_name': 'consulatation/consultation_form.html'}, name='add_social_form'),   # DONE
    url(r'^edit/social_service/(?P<pk>[-\d]+)$', login_required(views.UpdateSocialService.as_view()), name='edit_social_service'),   # DONE
    url(r'^edit/service/(?P<pk>[-\d]+)$', login_required(views.UpdateService.as_view()), name='edit_service'),   # DONE
    url(r'^profile/edit/org/$', login_required(views.UpdateOrg.as_view()), name='edit_org_form'),   # DONE
    url(r'^edit/event/(?P<pk>[-\d]+)$', login_required(views.UpdateEvent.as_view()), name="edit_event"),   # DONE
    url(r'^edit/consultation/(?P<pk>[-\d]+)$',login_required(views.UpdateConsultation.as_view()), name="edit_consultation"),   # Сюда отдельную форму
    url(r'^profile/edit/ms/(?P<pk>[-\d]+)/$', login_required(views.UpdateMSFormView.as_view()), name='edit_ms'),
    url(r'^profile/ms/add_point/(?P<pk>[-\d]+)/$', login_required(views.AddRouteMSFormView.as_view()), name='add_ms_point'),
    url(r'^profile/ms/edit_point/(?P<pk>[-\d]+)/$', login_required(views.UpdateRouteMSFormView.as_view()), name='edit_ms_point'),

    url(r'^send/event/(?P<pk>[-\d]+)$',login_required(views.SendEventNotificationFormView.as_view()), name="send_notification_event"),

    url(r'^delete/contact/(?P<pk>[-\d]+)$',login_required(views.DeleteContactView.as_view()), name="delete_org_contact"),

    url(r'^add/contact/$',login_required(views.CreateContactView.as_view()), name="add_org_contact"),
    url(r'^add/service/$', login_required(views.AddServiceFormView.as_view()), name='add_service_form'),    # DONE
    url(r'^add/seat/$', login_required(views.AddSeatFormView.as_view()), name='add_seat_form'),             # DONE
    url(r'^add/event/$', login_required(views.AddEventVFormView.as_view()), name='add_event_form'),         # DONE


    url(r'^profile/$', login_required(views.ProfileView.as_view(template_name="profile/profile_detail.html")), name='profile'),
    url(r'^profile/service/$', login_required(views.ProfileView.as_view(template_name='profile/profile_service.html')), name='profile_service'),
    url(r'^profile/seat/$', login_required(views.ProfileView.as_view(template_name='profile/profile_seat.html')), name='profile_seat'),
    url(r'^profile/event/$', login_required(views.ProfileView.as_view(template_name='profile/profile_event.html')), name='profile_event'),
    url(r'^profile/add/ms/$', login_required(views.AddMSFormView.as_view()), name='add_ms'),
    url(r'^profile/add/seat/$', login_required(views.ProfileView.as_view()), name='add_seat'),
    url(r'^profile/add/event/$', login_required(views.ProfileView.as_view()), name='add_event'),

    url(r'^certificate/$', login_required(views.CertificateView.as_view()), name='certificate'),
    url(r'^certificate/add/$', login_required(wizards.certificate_wizard), name='add_certificate'),
    url(r'^certificate/pdf/(?P<pk>[-\d]+)$', login_required(views.CertificatePdfView.as_view()), name="certificate_pdf"),
    url(r'^certificate/close/(?P<pk>[-\d]+)$', login_required(views.CloseCertificateView.as_view()), name="step_close"),
    url(r'^certificate/edit/(?P<pk>[-\d]+)$', login_required(views.UpdateCertificateView.as_view()), name="certificate_edit"),
    url(r'^certificate/(?P<pk>[-\d]+)$', login_required(views.CertificateDetailView.as_view()), name="certificate_detail"),

    url(r'^consultation/$', login_required(views.ConsultationView.as_view()), name='consultation'),
    url(r'^consultation/add/$',login_required(wizards.cons_wizard), name='add_consultation'),
    url(r'^consultation/archive/$', login_required(views.ConsultationArchiveView.as_view()), name='consultation_archive'),
    url(r'^consultation/(?P<pk>[-\d]+)$', login_required(views.ConsultationDetailView.as_view()), name="consultation_detail"),
    url(r'^consultation/pdf/(?P<pk>[-\d]+)$', login_required(views.ConsultationPdfView.as_view()), name="consultation_pdf"),
    url(r'^consultation/direction/$', login_required(views.RedirectionView.as_view()), name="redirection"),

    url(r'^add/patient_dinamic/$', views.AddPatientDinamicView.as_view(), name='add_patient_dinamic'),
    url(r'^add/patient/$', views.AddPatientView.as_view(), name='add_patient'),
    url(r'^add/orgs/$', views.JoinFormView.as_view(), name='add_orgs_form'),
    url(r'^accounts/logout/$', auth_views.logout, kwargs={'next_page': 'start_page'}, name='logout'),
    url(r'^accounts/login/$', auth_views.login, name='login_html'),
    url(r'^accounts/change_pass/$', auth_views.password_change, {'post_change_redirect' : '/profile/', 'template_name':'form/standart.html'}, name='change_pass'),

    url(r'^orgs/$', login_required(views.OrgsView.as_view()), name='orgs'),
    url(r'^orgs/(?P<pk>[-\d]+)$', login_required(views.OrgDetailView.as_view()), name='org_detail'),
    url(r'^orgs/social_service/(?P<pk>[-\d]+)$', login_required(views.SocialServiceDetailView.as_view(model=SocialService)), name='social_service_detail'),
    url(r'^event/$', login_required(views.EventView.as_view()), name='event'),
    url(r'^event/(?P<pk>[-\d]+)/$', login_required(views.EventDetailView.as_view()), name='event_detail'),
    url(r'^seat/$', login_required(views.SeatView.as_view()), name='seat'),
    url(r'^legislation/$', login_required(views.LegislationView.as_view()), name='legislation'),
    url(r'^legislation/(?P<pk>[-\d]+)$', login_required(views.LegislationDocsView.as_view()), name='legislation_doc'),

    url(r'^orgs/ms/(?P<pk>[-\d]+)$', login_required(views.MSDetailView.as_view()), name='ms_detail'),

    url(r'^user/$',
        login_required(views.UserProfileListView.as_view()),
        name='user_list'),

    url(r'^user/(?P<pk>[-\d]+)/$',
        login_required(views.UserProfileView.as_view()),
        name='user_profile'),

    url(r'^user/edit/$',
        login_required(views.UserUpdateView.as_view()),
        name='user_edit'),

    url(r'^blank/$',
        login_required(views.BlankListView.as_view()),
        name = 'blank_list'
    ),

    url(r'^blank/(?P<pk>[-\d]+)$',
        login_required(views.BlankDetailView.as_view()),
        name = 'blank_detail'
    ),

    url(r'^blank/(?P<blank>[-\d]+)/add_service_plan/$',
        login_required(views.AddBlankServicePlanFormView.as_view()),
        name = 'blank_add_service_plan'
    ),

    url(r'^blank/(?P<blank>[-\d]+)/(?P<pk>[-\d]+)/add_service/$',
        login_required(views.AddBlankServiceFormView.as_view()),
        name = 'blank_add_service'
    ),

    url(r'^blank/(?P<pk>[-\d]+)/add_family/$',
        login_required(views.AddFamilyMemberFormView.as_view()),
        name = 'blank_add_family'
    ),

    url(r'^blank/service/add/$',
        login_required(views.CreateBlankServiceItemView.as_view()),
        name = 'add_blank_service'
    ),

    url(r'^blank/service/(?P<pk>[-\d]+)/$',
        login_required(views.BlankServicePlanDetailView.as_view()),
        name = 'blank_service_plan_detail'
    ),

    url(r'^blank/add/$',
        login_required(wizards.blank_wizard),
        name='add_blank'),


    url(r'^reports/$',
        login_required(views.ReportView.as_view()),
        name='report'),

    url(r'^json/seat/$', login_required(views.SeatJson.as_view()), name='jsonSeat'),
    url(r'^json/orgs/$', views.OrgsJson.as_view(), name='jsonOrgs'),
    url(r'^json/event/$', login_required(views.EventJson.as_view()), name='jsonEvent'),
    url(r'^json/social_service/$', views.SocialServiceJson.as_view(), name='jsonSocialService'),
    url(r'^json/legislation/$', login_required(views.LegislationJson.as_view()), name='jsonLegislation'),
    url(r'^json/consultation/$', login_required(views.ConsultationJson.as_view()), name='jsonConsultation'),
    url(r'^json/direction/$', login_required(views.DirectionJson.as_view()), name='jsonDirection'),
    url(r'^json/certificate/$', login_required(views.CertificateJson.as_view()), name='jsonCertificate'),
    url(r'^json/patient/(?P<pk>[-\d]+)$', login_required(views.PatientJson.as_view()), name='jsonPatientList'),
    url(r'^debug/celery/$', login_required(views.DebugCelery.as_view()), name='debug_celery'),
)

if settings.DEBUG:
    urlpatterns += patterns(
        '',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT}))
