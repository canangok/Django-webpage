import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'houseofapps'
EMAIL_HOST_PASSWORD = 'password'
DEFAULT_FROM_EMAIL = ''
DEFAULT_TO_EMAIL = 'to email'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
