from django.contrib.staticfiles.storage import ManifestStaticFilesStorage

from .base import *  # noqa
from .base import env

# GENERAL
# ------------------------------------------------------------------------------

SECRET_KEY = env("DJANGO_SECRET_KEY")

ALLOWED_HOSTS = env.list("DJANGO_ALLOWED_HOSTS", default=["example.com"])

# DATABASES
# ------------------------------------------------------------------------------
DATABASES["default"] = env.db("DATABASE_URL")  # noqa F405
DATABASES["default"]["ATOMIC_REQUESTS"] = True  # noqa F405
DATABASES["default"]["CONN_MAX_AGE"] = env.int("CONN_MAX_AGE", default=60)  # noqa F405

# CACHES
# ------------------------------------------------------------------------------
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": env("REDIS_URL"),
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            # Mimicing memcache behavior.
            # http://niwinz.github.io/django-redis/latest/#_memcached_exceptions_behavior
            "IGNORE_EXCEPTIONS": True,
        },
    }
}

# CACHES = {
#     "default": {
#         "BACKEND": "django.core.cache.backends.memcached.MemcachedCache",
#         "LOCATION": "127.0.0.1:11211",
#     }
# }


# SECURITY
# ------------------------------------------------------------------------------
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
SECURE_SSL_REDIRECT = env.bool("DJANGO_SECURE_SSL_REDIRECT", default=True)
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

# TODO: set this to 60 seconds first and then to 518400 once you prove the former works
SECURE_HSTS_SECONDS = 60
SECURE_HSTS_INCLUDE_SUBDOMAINS = env.bool(
    "DJANGO_SECURE_HSTS_INCLUDE_SUBDOMAINS", default=True
)
SECURE_HSTS_PRELOAD = env.bool("DJANGO_SECURE_HSTS_PRELOAD", default=True)
SECURE_CONTENT_TYPE_NOSNIFF = env.bool(
    "DJANGO_SECURE_CONTENT_TYPE_NOSNIFF", default=True
)

# STORAGES
# ------------------------------------------------------------------------------
"""
INSTALLED_APPS += ["storages"]  # noqa F405
AWS_ACCESS_KEY_ID = env("DJANGO_AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = env("DJANGO_AWS_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME = env("DJANGO_AWS_STORAGE_BUCKET_NAME")
AWS_QUERYSTRING_AUTH = False
AWS_S3_CUSTOM_DOMAIN = f"{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com"
AWS_DEFAULT_ACL = "public-read"
# DO NOT change these unless you know what you're doing.
_AWS_EXPIRY = 60 * 60 * 24 * 7
AWS_S3_OBJECT_PARAMETERS = {
    "CacheControl": f"max-age={_AWS_EXPIRY}, s-maxage={_AWS_EXPIRY}, must-revalidate"
}

AWS_S3_REGION_NAME = env("DJANGO_AWS_S3_REGION_NAME", default=None)
# STATIC
# ------------------------
AWS_STATIC_LOCATION = "static"
STATIC_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/{AWS_STATIC_LOCATION}/"
STATICFILES_STORAGE = "config.storage_backends.StaticStorage"
# MEDIA
# ------------------------------------------------------------------------------
# AWS S3 Public Media Upload
AWS_MEDIA_LOCATION = "media"
MEDIA_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/{AWS_MEDIA_LOCATION}/"
DEFAULT_FILE_STORAGE = "config.storage_backends.MediaStorage"
"""


class ForgivingManifestStaticFilesStorage(ManifestStaticFilesStorage):
    manifest_strict = False
    # def hashed_name(self, name, content=None, filename=None):
    #     try:
    #         result = super().hashed_name(name, content, filename)
    #     except ValueError:
    #         # When the fille is missing, let's forgive and ignore that.
    #         print(f'"{name}" not found ...')
    #         result = name
    #     return result


# STATICFILES_STORAGE = "django.contrib.staticfiles.storage.ManifestStaticFilesStorage"
STATICFILES_STORAGE = "config.settings.production.ForgivingManifestStaticFilesStorage"

# TEMPLATES
# ------------------------------------------------------------------------------
# TEMPLATES[0]["OPTIONS"]["loaders"] = [  # noqa F405
#     (
#         "django.template.loaders.cached.Loader",
#         [
#             "django.template.loaders.filesystem.Loader",
#             "django.template.loaders.app_directories.Loader",
#         ],
#     )
# ]

# ADMIN
# ------------------------------------------------------------------------------
# Django Admin URL regex.
ADMIN_URL = env("DJANGO_ADMIN_URL")

# Collectfast
# ------------------------------------------------------------------------------
INSTALLED_APPS = ["collectfast"] + INSTALLED_APPS  # noqa F405
COLLECTFAST_STRATEGY = "collectfast.strategies.filesystem.FileSystemStrategy"

# LOGGING
# ------------------------------------------------------------------------------

# See https://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.

LOGGING = {
    "version": 1,
    "disable_existing_loggers": True,
    "formatters": {
        "verbose": {
            # "format": "%(levelname)s %(asctime)s %(module)s "
            # "%(process)d %(thread)d %(message)s"
            "format": "%(asctime)s  [%(name)s:%(module)s:%(lineno)s]  %(levelname)s - %(message)s"
        }
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        }
    },
    "root": {"level": "INFO", "handlers": ["console"]},
    "loggers": {
        "django.db.backends": {
            "level": "ERROR",
            "handlers": ["console"],
            "propagate": False,
        },
    },
}


# Your stuff...
# ------------------------------------------------------------------------------

FILE_UPLOAD_DIRECTORY_PERMISSIONS = 0o755
FILE_UPLOAD_PERMISSIONS = 0o644

# print(MEDIA_ROOT)
