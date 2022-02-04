from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'b2au3usfjhbge4k',
        'CLIENT': {
            'host': 'mongodb://u1w5moexap6rxyfdeeea:GfA2wmRMYURJABPQkKcf@b2au3usfjhbge4k-mongodb.services.clever-cloud.com:27017/b2au3usfjhbge4k',
        }
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'