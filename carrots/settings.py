"""
Django settings for carrots project.

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
SECRET_KEY = '&#x%5x6qk$qhpi0f-%6f1844b+^q_c8te@-gd8g0vipq!r-s9p'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Logowanie z na podstawie info od fejsika
AUTHENTICATION_BACKENDS = (
'django.contrib.auth.backends.ModelBackend',
'social_auth.backends.facebook.FacebookBackend',
)

FACEBOOK_APP_ID = 231250787038938
FACEBOOK_API_SECRET = 'c35bc84bf62bfbba87c71b9fd358c12e'

LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/polls/' # tutaj ma trafic u ´ zytkownik zaraz po zalogowaniu ˙
LOGIN_ERROR_URL = '/login/'

SESSION_SERIALIZER = 'django.contrib.sessions.serializers.PickleSerializer'

FACEBOOK_AUTH_EXTRA_ARGUMENTS = {'scope': 'publish_stream'}


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'polls',
    'social_auth',
    'account'

)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'carrots.urls'

WSGI_APPLICATION = 'carrots.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'carrots.db',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'pl'

TIME_ZONE = 'Europe/Warsaw'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
