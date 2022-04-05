"""
Django settings for litigation_management_software project.

Generated by 'django-admin startproject' using Django 3.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import os
from django.utils.translation import gettext_lazy as _

from django.conf.locale.es import formats as es_formats

LANGUAGE_CODE = 'en'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = False
USE_TZ = True

LANGUAGES = (
    ('en', _('English')),
    ('it', _('Italian'))
)

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '=r0hr+xb)+7bf-o23mp#(=s=b*tnjd57hd(xwh8463(!i!+(r_'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# ALLOWED_HOSTS = ['146.148.10.6', 'localhost', '127.0.0.1']
ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'material',
    # 'django.contrib.admin',
    'admin_panel.apps.CustomAdminConfig',  # customized dashboard
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #
    'attachments',  # any file. Used for attaching contract
    'import_export',  # xlsx for cost statement
    #
    'clients',  # clients.apps.ClientsConfig
    'lawyers',
    'litigations.apps.LitigationsConfig',
    'costStatements',
    'contracts',
    'configurations',
    'notifications',
    'statistics_page.apps.StatisticsPageConfig',
    'KPI',
    'rosetta',

]
ROSETTA_SHOW_AT_ADMIN_PANEL = True

MIGRATION_MODULES = {
    'translator': 'admin_panel.translator_migrations',
}

DELETE_ATTACHMENTS_FROM_DISK = True

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

X_FRAME_OPTIONS = 'SAMEORIGIN'

ROOT_URLCONF = 'admin_panel.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates/"), ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ]
        }
    },
]

WSGI_APPLICATION = 'admin_panel.wsgi.application'

# OUTGOING MAIL SERVER
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

# PRODUCTION
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'litigation_management',
#         'HOST': '/opt/bitnami/mariadb/tmp/mysql.sock',
#         'PORT': '3306',
#         'USER': 'root',
#         'PASSWORD': 'M9FpH8J7Nmb7'
#     }
# }

# DEVELOPMENT
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# TEST
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'django',
#         'USER': 'openpg',
#         'PASSWORD': 'openpg',
#         'HOST': 'localhost',
#         'PORT': '5432',
#     }
# }

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

PRODUCTION_MODE = True

if PRODUCTION_MODE:
    MEDIA_URL = 'https://projects.gridcoding.com/defynd/media/'
    STATIC_URL = 'https://projects.gridcoding.com/defynd/static/'
else:
    MEDIA_URL = '/media/'
    STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]

STATIC_ROOT = os.path.join(BASE_DIR, "assets")
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'admin_panel', 'locale'),
)

DATE_INPUT_FORMATS = ['%d/%m/%Y']
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = '587'
EMAIL_HOST_USER = "kosta.anxhela93@gmail.com"
EMAIL_HOST_PASSWORD = "albertos1nan1"
EMAIL_USE_TLS = True
