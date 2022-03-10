from pathlib import Path
# from django.db.backends import postgresql
from django.contrib import messages
import os
import environ

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'sdgsdgsddshfddfshsfdhsgjs'

DEBUG = True

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'Sinov',
        'USER': 'abbos',
        'PASSWORD': 'ilovedarknet',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
# Application definition
 
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'main',
    'client',
    'crispy_forms',


]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'templates'
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'



# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases



# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'uz-UZ'

TIME_ZONE = 'Asia/Tashkent'

USE_I18N = True

USE_L10N = True

USE_TZ = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'static'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'


AUTH_USER_MODEL = 'client.User'

# INTERNAL_IPS = [
#     '127.0.0.1'
# ]

MESSAGE_TAGS = {
     messages.INFO: "alert alert-info",
     messages.WARNING: "alert alert-warning",
     messages.ERROR: "alert alert-danger",
     messages.SUCCESS: "alert alert-success",
     messages.DEBUG: "alert alert-dark"
}

CRISPY_TEMPLATE_PACK = 'bootstrap4'

STATICFILES_DIRS = [
    BASE_DIR / 'assets'
]

LANGUAGES = (
    ('uz', "O'zbek 🇺🇿"),
    ('ru', "Русский 🇷🇺")
)


SETTINGS_EXPORT = [
    "LANGUAGES"
]


LOCALE_PATHS = [
    BASE_DIR / 'locale'
    ]

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
