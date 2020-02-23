import os
from dotenv import load_dotenv
load_dotenv()
import environs
#import dj_database_url

env = environs.Env()


#DATABASES = {'default': dj_database_url.config(default=os.environ['DATABASE_URL'])}

DATABASES = {
    'default': {
        'ENGINE': os.getenv('ENGINE'),
        'HOST': os.getenv('DB_HOST'),
        'PORT': os.getenv('DB_PORT'),
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD')
    }
}



INSTALLED_APPS = ['datacenter']

SECRET_KEY = os.getenv('SECRET_KEY')

DEBUG = env.bool('DEBUG', default=False)

ROOT_URLCONF = "project.urls"

ALLOWED_HOSTS = ['*']

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
    },
]


USE_L10N = True

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_TZ = True
