from pathlib import Path
import os



BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-91!sohpw=^0$l#2&_+9+^nt0+ht@+x4qlfva$ej(i*(+src6&y'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

CSRF_TRUSTED_ORIGINS = ['https://store-production-87fe.up.railway.app']
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'main',
  
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

ROOT_URLCONF = 'Ikko.urls'

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

WSGI_APPLICATION = 'Ikko.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators



if DEBUG:
    AUTH_PASSWORD_VALIDATORS = []
else: 
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

LOGIN_REDIRECT_URL = 'main/index.html'

# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

# Налаштування статичних файлів
STATIC_URL = '/static/'  # URL для статичних файлів
STATIC_ROOT = BASE_DIR / 'staticfiles'  # Де зберігаються зібрані статичні файли (production)
STATICFILES_DIRS = [
    BASE_DIR / 'main' / 'static',  # Додаткові каталоги для статичних файлів
]

# Налаштування медіа файлів
MEDIA_URL = '/media/'  # URL для медіа файлів
MEDIA_ROOT = BASE_DIR / 'main' / 'media'  # Де зберігаються медіа файли


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

STRIPE_PUBLIC_KEY = "pk_test_51OkvwiLjk5YNkIsHXf8bBEejMbIsAFr4hWx9YBEwpvFzP9eK3P8tCrvUzkYI2XnMY4rknYsVPF9iho185xIZ9cOP00jOZcgZLQ"  
STRIPE_SECRET_KEY = "sk_test_51OkvwiLjk5YNkIsHf9NcnSBdxxqg8oT1CNMyEmpGVI69olsEgPW0jmze4i8XHAfRwB4RjpTtlqMgjx36QlZ8cXQ800VFoDIIQd"
STRIPE_WEBHOOK_SECRET = ""


# EMAIL_BACKEND = 'django.core.mail.backends.db.EmailBackend'
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'    
# EMAIL_HOST = 'smtp.gmail.com'  
# EMAIL_PORT = 587  
# EMAIL_USE_TLS = True  
# EMAIL_HOST_USER = 'markizkit3@gmail.com'  
# EMAIL_HOST_PASSWORD = '*' 