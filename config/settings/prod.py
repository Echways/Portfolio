from .base import *
from config.core.env import get_bool, get_int, get_list, get_str


DEBUG = False

ALLOWED_HOSTS = ALLOWED_HOSTS or ["localhost"]
CSRF_TRUSTED_ORIGINS = get_list("DJANGO_CSRF_TRUSTED_ORIGINS")

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
SECURE_SSL_REDIRECT = get_bool("DJANGO_SECURE_SSL_REDIRECT", True)
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SAMESITE = get_str("DJANGO_SESSION_COOKIE_SAMESITE", "Lax")
CSRF_COOKIE_SAMESITE = get_str("DJANGO_CSRF_COOKIE_SAMESITE", "Lax")
SECURE_HSTS_SECONDS = get_int("DJANGO_SECURE_HSTS_SECONDS", 31536000)
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_REFERRER_POLICY = get_str("DJANGO_SECURE_REFERRER_POLICY", "same-origin")
SECURE_CROSS_ORIGIN_OPENER_POLICY = get_str("DJANGO_SECURE_COOP", "same-origin")
X_FRAME_OPTIONS = "DENY"

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
        "level": get_str("DJANGO_LOG_LEVEL", "INFO"),
    },
    "loggers": {
        "django": {
            "handlers": ["console"],
            "level": get_str("DJANGO_LOG_LEVEL", "INFO"),
            "propagate": False,
        },
    },
}
