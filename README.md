PROJECT_TITLE="Quickly Grocery App"

# PostgreSQL
DATABASE_URL=postgres://postgres:password@localhost:5432/quickly_grocery_app

# General
# ------------------------------------------------------------------------------
# DJANGO_READ_DOT_ENV_FILE=True
DJANGO_SETTINGS_MODULE=config.settings.local
DJANGO_SECRET_KEY=l+r0b4%#_&*75*%*kfk5w4epc$ms9aeikk2wzn2uaep(d!r_m8
DJANGO_ADMIN_URL=!!!SET DJANGO_ADMIN_URL!!!
DJANGO_ALLOWED_HOSTS=.example.com

DJANGO_READ_DOT_ENV_FILE=True

# Security
# ------------------------------------------------------------------------------
# TIP: better off using DNS, however, redirect is OK too
DJANGO_SECURE_SSL_REDIRECT=False

# Email
# ------------------------------------------------------------------------------
DJANGO_SERVER_EMAIL=


# AWS
# ------------------------------------------------------------------------------
DJANGO_AWS_ACCESS_KEY_ID=
DJANGO_AWS_SECRET_ACCESS_KEY=
DJANGO_AWS_STORAGE_BUCKET_NAME=

# django-allauth
# ------------------------------------------------------------------------------
DJANGO_ACCOUNT_ALLOW_REGISTRATION=True

# Gunicorn
# ------------------------------------------------------------------------------
WEB_CONCURRENCY=4


# Redis
# ------------------------------------------------------------------------------
REDIS_URL=redis://redis:6379/0

# Celery
# ------------------------------------------------------------------------------
# CELERY_BROKER_URL=amqp://guest:guest@localhost:5672/
CELERY_BROKER_URL=redis://redis:6379/0

# Flower
CELERY_FLOWER_USER=!!!SET CELERY_FLOWER_USER!!!
CELERY_FLOWER_PASSWORD=!!!SET CELERY_FLOWER_PASSWORD!!!

# Mail Configuration
# ------------------------------------------------------------------------------
EMAIL_HOST='smtp.gmail.com'
EMAIL_PORT=587
EMAIL_USE_TLS=True    
EMAIL_ADMIN_NAME=
EMAIL_HOST_USER=
EMAIL_HOST_PASSWORD=
