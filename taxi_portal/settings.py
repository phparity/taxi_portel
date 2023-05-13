"""
Django settings for taxi_portal project.

Generated by 'django-admin startproject' using Django 4.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os
from osgeo import gdal
#  from django.contrib.gis import gdal

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-)(!#1+=uk)d#j9gwq-3*ws594c_=xh!v@$di81ty9cg5(^r53w"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []
# http://demoby.arityinfoway.com:8000/
# 'localhost','143.110.153.4','*','192.168.192.115','demoby.arityinfoway.com'
# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django_google_maps",
    "location_field.apps.DefaultConfig",
    "app1",
    "ckeditor",
    "fontawesome_5",
    'django_otp',
    'django_otp.plugins.otp_totp',
    # "django.contrib.gis",
   
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    'django_otp.middleware.OTPMiddleware',
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "taxi_portal.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, 'templates')],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "taxi_portal.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases
 # "ENGINE": "django.db.backends.sqlite3",


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite31",
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

# STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'app1', 'static'),
]

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
# STATICFILES_DIRS = [
#    os.path.join(BASE_DIR, "static"),
#    ]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# GDAL_LIBRARY_PATH = '/path/to/your/gdal/library'  # Update with the correct path to the GDAL library on your system
# GDAL_LIBRARY_PATH = r"C:\OSGeo4W\bin\geos_c.dll"         #r"C:\OSGeo4W\bin\gdal306.dll"

# GOOGLE_MAPS_API_KEY = 'AIzaSyAwpOVKBbLxRTSIJyKeZzeBQlLJNetx480'

# GOOGLE_MAPS_API_KEY ='AIzaSyBeQUngByPnQY_2khrrGcD1guFKO9krDuk'

GOOGLE_MAPS_API_KEY ='AIzaSyBeQUngByPnQY_2khrrGcD1guFKO9krDuk'

# GDAL_LIBRARY_PATH = r"C:\OSGeo4W\bin\gdal306.dll"
# GEOS_LIBRARY_PATH =  r"C:\OSGeo4W\bin\geos_c.dll"
# #
# 
# 


# GDAL_LIBRARY_PATH = r'C:\OSGeo4W\bin\gdal306'
# GEOS_LIBRARY_PATH = os.environ.get("GEOS_LIBRARY_PATH")
# GEOS_LIBRARY_PATH = r'C:\OSGeo4W\bin\geos_c.dll'                  
# Proj_LIBRARY_PATH = r"C:\OSGeo4W\bin\proj_9_2.dll"
# GDAL_LIBRARY_PATH = r'C:\OSGeo4W\bin\gdal306'
# GDAL_LIBRARY_PATH = os.environ.get(r'C:\OSGeo4W\bin\gdal306')
# GDAL_LIBRARY_PATH = r"C:\OSGeo4W\bin\gdal306.dll"

# if os.name == 'nt':
#     import platform
#     OSGEO4W = r"C:\OSGeo4W"
#     if '64' in platform.architecture()[0]:
#         OSGEO4W += "64"
#     assert os.path.isdir(OSGEO4W), "Directory does not exist: " + OSGEO4W
#     os.environ['OSGEO4W_ROOT'] = OSGEO4W
#     os.environ['GDAL_DATA'] = OSGEO4W + r"\share\gdal"  
#     os.environ['PROJ_LIB'] = OSGEO4W + r"\share\proj"
#     os.environ['PATH'] = OSGEO4W + r"\bin;" + os.environ['PATH']
# GDAL_LIBRARY_PATH = r'C:\OSGeo4W\bin\gdal306.dll'
# GEOS_LIBRARY_PATH = r'C:\OSGeo4W\bin\geos_c.dll'


EMAIL_HOST = "smtp.gmail.com"
EMAIL_HOST_USER = "arity.php@gmail.com"
EMAIL_HOST_PASSWORD = "oohjltyincnyhvep"
EMAIL_PORT = 587
EMAIL_USE_TLS = True


