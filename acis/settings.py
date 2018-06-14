"""
Django settings for acis project.

Generated by 'django-admin startproject' using Django 1.11.3.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'y+cz5bss=pao3ehe*v$5u+5d8yoo99)9&bm1+&=fnzxfznbg=r'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Application definition
INSTALLED_APPS = [
    'django.contrib.sites',
    'django.contrib.auth',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'polymorphic',
    'django.contrib.contenttypes',
    'taggit',
    'mptt',
    'cms',
    'django.contrib.admin',
    'ckeditor',
    'ckeditor_uploader',
    'django_bleach',
    'ban',
    'djangobower',
    'pybb',
    'django_messages',
    'captcha'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'ban.middleware.BanManagement',
    'pybb.middleware.PybbMiddleware'
]

ROOT_URLCONF = 'acis.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
                'pybb.context_processors.processor'
            ],
        },
    },
]

WSGI_APPLICATION = 'acis.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'postgres',
        'PORT': 5432
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
]

# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'uk'

LANGUAGES = (
    ('ru', 'Russian'),
    ('en', 'English'),
    ('uk', 'Ukrainian'),
)

TIME_ZONE = 'Europe/Kiev'

USE_I18N = True

USE_L10N = True

USE_TZ = True

SITE_ID = 1

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'djangobower.finders.BowerFinder',
)

BOWER_COMPONENTS_ROOT = os.path.join(BASE_DIR, './')
BOWER_INSTALLED_APPS = (
    'jquery#3.3',
    'jquery-ui#1.12',
    'jquery.tagsinput#1.3.6',
    'fancybox#3.3.5',
)

FILE_UPLOAD_PERMISSIONS = 0o755
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
CKEDITOR_UPLOAD_PATH = 'uploads/'
CKEDITOR_ALLOW_NONIMAGE_FILES = False

ACCOUNT_ACTIVATION_DAYS = 2
REGISTRATION_OPEN = True
REGISTRATION_SALT = 'FfjoH3YJSavC67d6MvZCzAUGZJluMJqYlZ10WqLfPM79uydOe4CqMQMuJWeie9yA'

EMAIL_HOST = 'postfix'
EMAIL_PORT = 25
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_USE_TLS = False
DEFAULT_FROM_EMAIL = 'info@diggers.kiev.ua'

#HOME_CATEGORY_ROUTE = 'news'
MAPS_CATEGORY_ROUTE = 'map'

BLEACH_ALLOWED_TAGS = [
  'p',
  'b',
  'i',
  'u',
  'em',
  'strong',
  'a',
  'table',
  'tr',
  'td',
  'th',
  'thead',
  'tbody',
  'caption',
  'hr',
  'span',
  'img'
]
BLEACH_ALLOWED_ATTRIBUTES = ['href', 'title', 'style', 'cellpadding', 'cellspacing', 'border', 'target', 'alt', 'src']
BLEACH_ALLOWED_STYLES = [
  'font-family',
  'font-weight',
  'text-decoration',
  'font-variant',
  'background-color',
  'border-color',
  'border-style',
  'border-width',
  'float',
  'text-align',
  'vertical-align',
  'width',
  'height',
  'width',
  'color',
  'margin'
]
BLEACH_STRIP_TAGS = True
BLEACH_STRIP_COMMENTS = False

AVATAR_MAX_WIDTH = 60
AVATAR_MAX_HEIGHT = 60

DEFAULT_REGISTRATION_GROUP = 'Пользователи'

PAGINATION_POSTS_COUNT = 25

PREMODERATION_CATEGORIES = ['map', 'news']
PREMODERATION_GROUPS = ['Пользователи', 'Пользователи с доступом к закрытым разделам']

SESSION_SAVE_EVERY_REQUEST = True

ALLOWED_HOSTS = [
    'web',
]

PYBB_TEMPLATE = 'cms/base.html'
PYBB_MARKUP = 'bbcode'
PYBB_DEFAULT_TITLE = 'Форум'
PYBB_DEFAULT_AUTOSUBSCRIBE = False
PYBB_AVATAR_WIDTH = 60
PYBB_AVATAR_HEIGHT = 60
PYBB_DEFAULT_TIME_ZONE = 2
PYBB_SIGNATURE_MAX_LENGTH = 400
PYBB_ATTACHMENT_ENABLE = True
PYBB_ENABLE_ADMIN_POST_FORM = False

RECAPTCHA_PUBLIC_KEY = '6LegnF0UAAAAAIbP1Xu21W_e6kObQIOYbqFs2VBC'
RECAPTCHA_PRIVATE_KEY = '6LegnF0UAAAAAONkfdiI5dU1MhqA2BAvQsaGI2bp'
NOCAPTCHA = True