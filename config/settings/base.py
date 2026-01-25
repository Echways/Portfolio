from . import BASE_DIR
from config.core.env import get_bool, get_int, get_list, get_str


SECRET_KEY = get_str("DJANGO_SECRET_KEY", "dev-secret-key")

DEBUG = get_bool("DJANGO_DEBUG", True)

ALLOWED_HOSTS = get_list("DJANGO_ALLOWED_HOSTS")


INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "config.core.apps.CoreConfig",
    "info.apps.InfoConfig",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
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

WSGI_APPLICATION = "config.wsgi.application"
ASGI_APPLICATION = "config.asgi.application"


DB_ENGINE = get_str("DJANGO_DB_ENGINE", "sqlite")

if DB_ENGINE == "postgres":
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": get_str("DJANGO_DB_NAME", "portfolio"),
            "USER": get_str("DJANGO_DB_USER", "postgres"),
            "PASSWORD": get_str("DJANGO_DB_PASSWORD", "postgres"),
            "HOST": get_str("DJANGO_DB_HOST", "127.0.0.1"),
            "PORT": get_int("DJANGO_DB_PORT", 5432),
        }
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / get_str("DJANGO_DB_NAME", "db.sqlite3"),
        }
    }


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


LANGUAGE_CODE = get_str("DJANGO_LANGUAGE_CODE", "ru-ru")
TIME_ZONE = get_str("DJANGO_TIME_ZONE", "Europe/Moscow")
USE_I18N = True
USE_TZ = True


STATIC_URL = "static/"
STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_ROOT = BASE_DIR / "staticfiles"

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"


DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "standard": {
            "format": "%(asctime)s %(levelname)s %(name)s %(message)s",
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "standard",
        },
    },
    "root": {
        "handlers": ["console"],
        "level": get_str("DJANGO_LOG_LEVEL", "DEBUG" if DEBUG else "INFO"),
    },
}
