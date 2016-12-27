# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS

SITE_ID = 1
SITE_URL = "www.srnzspb.ru"

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '*%rbv#h!7w4p4kpsnpgimp^@_*p_%x2_)_ssg1#69vv11&70&a'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = [
    'srnzspb.ru',
    'www.srnzspb.ru',
    'family.hi-it.spb.ru',
]

ADMINS = (
    ('Boris Savelev', 'boris@dom-com.net'),
)

# Application definition

INSTALLED_APPS = (
    'grappelli',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'django_extensions',
    'qrcode',
    'easy_select2',
    'bootstrap3',
    'core',
    'public',
    'pytils',
    'djcelery',
    'tinymce',
    'imagekit',
    'django_messages',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS += (
    'django.core.context_processors.request',
    'core.context_processors.git_sha_id',
    'django_messages.context_processors.inbox',
)

ROOT_URLCONF = 'family.urls'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

TEMPLATE_DIRS = (os.path.join(os.path.dirname(__file__), '..', 'templates').replace('\\','/'),)

WSGI_APPLICATION = 'family.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'var', 'static')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'var', 'media')

LOCALE_PATHS = ('locale',)

DEFAULT_FROM_EMAIL = "srnzspb@yandex.ru"

# Celery

import djcelery

djcelery.setup_loader()
CELERY_REDIS_PORT = 6379
CELERY_REDIS_HOST = "localhost"
CELERY_REDIS_DB = 2
REDIS_CONNECT_RETRY = True
CELERY_SEND_EVENTS = True
CELERY_RESULT_BACKEND = 'redis'
CELERY_TASK_RESULT_EXPIRES = 10
CELERND_TASK_ERROR_EMAILS = True
BROKER_URL = "redis://localhost:6379/2"
CELERYBEAT_SCHEDULER = "djcelery.schedulers.DatabaseScheduler"

#Local setting

try:
    from local_setting import *
except ImportError:
    pass

DEFAULT_USER_PIC = STATIC_URL+ 'img/user.png'