"""
Django settings for main project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '+t%cc5jq-rg+=#9%(qzer83=dwv1$u@oplo*1@+cmc3_^*-ag4'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
DEBUG = True

#TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

# DJANGO COOKIE CONSENT
    'cookie_consent',

# APP LIST
    'video',
    'login',
    'jobs',
    'smhouse',
    'galery',
    'idea',

# MAP PLOTTING APP
    'mapplot',

# ZOOM buttons
#    'button',

# DJANGO CLEANUP
    'django_cleanup',
# MOBILE BROWSER DETECT
    'django_user_agents',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.sites.middleware.CurrentSiteMiddleware',

    'django_user_agents.middleware.UserAgentMiddleware',

    'main.last_seen.SetLastVisitMiddleware'
#    'main.last_seen.TestMiddleware'
]

ROOT_URLCONF = 'main.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
                '/home/alex/web22/template', '/home/alex/web22/video/template', '/home/alex/web22/login/template', '/home/alex/web22/jobs/template',
                '/home/alex/web22/smhouse/template', '/home/alex/web22/idea/template', '/home/alex/web22/galery/template',
		'/home/alex/web22/mapplot/template',

#                '/var/www/svabis.eu/template', '/var/www/svabis.eu/video/template', '/var/www/svabis.eu/login/template', '/var/www/svabis.eu/jobs/template',
#                '/var/www/svabis.eu/smhouse/template', '/var/www/svabis.eu/idea/template', '/var/www/svabis.eu/galery/template',
#		 '/var/www/svabis.eu/mapplot/template',

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

WSGI_APPLICATION = 'main.wsgi.application'
#WSGI_APPLICATION = 'wsgi.application'

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django_db',
        'USER': 'django',
        'PASSWORD': 'Dj2ng0',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/


LANGUAGE_CODE = 'lv'

TIME_ZONE = 'EET'

TIME_INPUT_FORMATS = [
    '%I:%M:%S %p',  # 6:22:44 PM
    '%I:%M %p',  # 6:22 PM
    '%I %p',  # 6 PM
    '%H:%M:%S',     # '14:30:59'
    '%H:%M:%S.%f',  # '14:30:59.000200'
    '%H:%M',        # '14:30'
]

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

#STATICFILES_DIRS = [ os.path.join(BASE_DIR, "static"), '/var/www/svabis.eu/static/', ]
#STATIC_ROOT = '/var/www/svabis.eu/static/'
STATIC_URL = '/static/'

STATICFILES_DIRS = [
        os.path.join(BASE_DIR, "static"),
        '/var/www/svabis.eu/static/',
    ]

MEDIA_ROOT = '/var/www/svabis.eu/media/'
MEDIA_URL = '/media/'
