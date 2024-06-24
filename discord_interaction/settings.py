"""
Django settings for discord_interaction project.

Generated by 'django-admin startproject' using Django 5.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path
from django.conf import settings
import os
import dj_database_url
import django_heroku


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-3$a6x$k02b6077fk@-8t!-x1q+ifcd(s&cd8jz(y3)j=c0=q!^'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1', '.ngrok.io', 'discordapp.com', '53c6-2806-2f0-4400-4008-b182-bf0b-ef79-aec3.ngrok-free.app', '4ffc-2806-2f0-4400-4008-b182-bf0b-ef79-aec3.ngrok-free.app', 'favicon.ico', '6750-2806-2f0-4400-4008-b182-bf0b-ef79-aec3.ngrok-free.app', '93db-2806-2f0-4400-4008-b182-bf0b-ef79-aec3.ngrok-free.app', 'https://500b-2806-2f0-4400-4008-b182-bf0b-ef79-aec3.ngrok-free.app', 'https://c45a-2806-2f0-4400-4008-b182-bf0b-ef79-aec3.ngrok-free.app', 'ngrok-free.app', 'c45a-2806-2f0-4400-4008-b182-bf0b-ef79-aec3.ngrok-free.app', 'good-man-close.ngrok-free.app', 'discord-interaction-ba1ec86e5d8e.herokuapp.com', 'gwenactivites.online']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.humanize',
    'corsheaders',
    'interactions',
    'discord_interaction',
    
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

CORS_ALLOWED_ORIGINS = [
    'http://localhost:8000',
    'http://127.0.0.1:8000',
    'https://discordapp.com',
    'https://good-man-close.ngrok-free.app',
    'https://subdomain.ngrok-free.app',
    'https://c45a-2806-2f0-4400-4008-b182-bf0b-ef79-aec3.ngrok-free.app',
    'https://gwenactivites.online',
]

ROOT_URLCONF = 'interactions.urls'

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
            ],
        },
    },
]

WSGI_APPLICATION = 'discord_interaction.wsgi.application'
CSRF_COOKIE_SECURE = False
CSRF_COOKIE_HTTPONLY = False

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

# Default to using SQLite for local development
DATABASES = {
    'default': dj_database_url.config(default=os.environ.get('postgres://uc67brmbo0sn72:p9c159a42672183ecd8164c5a9ce7a9a922eb2eb17545918266793790c53ae4c0@cd1goc44htrmfn.cluster-czrs8kj4isg7.us-east-1.rds.amazonaws.com:5432/d73q7i4q0ge7vo')),

}

# If DATABASE_URL is set in the environment, use that instead
if 'DATABASE_URL' in os.environ:
    DATABASES['default'] = dj_database_url.config(conn_max_age=600, ssl_require=True)

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'debug.log',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}
django_heroku.settings(locals())