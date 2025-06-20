from pathlib import Path
import os
from django.core.management.utils import get_random_secret_key
import sys
import dj_database_url
from storages.backends.s3boto3 import S3Boto3Storage
from datetime import timedelta

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
print(f"BASE_DIR: {BASE_DIR}")


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-3j96hah3@7@8b=o%q8gvmt-%_yx-wo^+m%3-pq1k9o66e%5_p+"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
DEVELOPMENT_MODE= False

ALLOWED_HOSTS = ["*"]
# Application definition


import os

if DEVELOPMENT_MODE is True:
     DATABASES = {
     "default": {
         "ENGINE": "django.db.backends.sqlite3",
         "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
     }
 }
else: 
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'mea',
            'USER': 'doadmin',
            'PASSWORD': 'AVNS_tX4w6erHeU_O1e_pOE-',
            'HOST': 'app-807a9868-54c1-4871-bfbd-504a8a4bba0a-do-user-244201-0.h.db.ondigitalocean.com',
            'PORT': '25061',
            'OPTIONS': {'sslmode': 'require'},
        }
    }




INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "rpm.apps.RpmConfig",
    "graphene_django",
    'graphql_jwt',
    "partners.apps.PartnersConfig"
] 

MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware', # new line added
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

]

GRAPHENE = {
#Add the line below
  'MIDDLEWARE': [
  'graphql_jwt.middleware.JSONWebTokenMiddleware',
],
}

GRAPHQL_JWT = {
'JWT_VERIFY_EXPIRATION': False,
 'JWT_EXPIRATION_DELTA': timedelta(minutes=1),
}

AUTHENTICATION_BACKENDS = [
 'graphql_jwt.backends.JSONWebTokenBackend',
'django.contrib.auth.backends.ModelBackend',
]


ROOT_URLCONF = 'RPM_Backend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'RPM_Backend.wsgi.application'

# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases




# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = BASE_DIR / 'staticfiles'


STATICFILES_DIRS = [BASE_DIR / 'rpm' / "static"]

GRAPHENE = {
    'SCHEMA' : 'rpm.schema.schema'
}
# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

class MediaStorage(S3Boto3Storage):

    location = 'media'
    file_overwrite = False

AWS_ACCESS_KEY_ID = 'DO006KHV8GFEZPAVRTVX'
AWS_SECRET_ACCESS_KEY = 'OKkCSBAUpIXR0zQ7gCRHvlDWG4x0PrKyrwnxu2n97eU'
AWS_STORAGE_BUCKET_NAME = 'mea-summit'
AWS_S3_REGION_NAME = 'fra1'  # Example: 'fra1'
AWS_S3_CUSTOM_DOMAIN = f"mea-summit.fra1.cdn.digitaloceanspaces.com"
AWS_S3_ENDPOINT_URL = "https://mea-summit.fra1.digitaloceanspaces.com"
AWS_DEFAULT_ACL = 'public-read'
AWS_LOCATION = ''
PUBLIC_MEDIA_LOCATION = ''
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
