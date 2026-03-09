"""
Django settings for portfolio project.
Production ready for stevedev.live
"""

from pathlib import Path
from decouple import Config, RepositoryEnv
import os

BASE_DIR = Path(__file__).resolve().parent.parent

# =====================================================
# ENV CONFIG
# =====================================================

env = Config(RepositoryEnv(BASE_DIR / ".env"))

SECRET_KEY = env("DJANGO_SECRET_KEY")

DEBUG = env("DJANGO_DEBUG", default=False, cast=bool)

ALLOWED_HOSTS = [
    "127.0.0.1",
    "localhost",
    "13.60.83.201",
    "stevedev.live",
    "www.stevedev.live",
]

# =====================================================
# APPLICATIONS
# =====================================================

INSTALLED_APPS = [

    "jazzmin",

    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    "rest_framework",
    "corsheaders",

    "apps.blogs",
    "apps.skills",
    "apps.profiles",
]

# =====================================================
# MIDDLEWARE
# =====================================================

MIDDLEWARE = [

    "corsheaders.middleware.CorsMiddleware",

    "django.middleware.security.SecurityMiddleware",

    # Static files middleware
    "whitenoise.middleware.WhiteNoiseMiddleware",

    "django.contrib.sessions.middleware.SessionMiddleware",

    "django.middleware.common.CommonMiddleware",

    "django.middleware.csrf.CsrfViewMiddleware",

    "django.contrib.auth.middleware.AuthenticationMiddleware",

    "django.contrib.messages.middleware.MessageMiddleware",

    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "portfolio.urls"

WSGI_APPLICATION = "portfolio.wsgi.application"

# =====================================================
# TEMPLATES
# =====================================================

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
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

# =====================================================
# DATABASE (MYSQL)
# =====================================================

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": env("DB_NAME"),
        "USER": env("DB_USER"),
        "PASSWORD": env("DB_PASSWORD"),
        "HOST": env("DB_HOST"),
        "PORT": env("DB_PORT", cast=int),
        "OPTIONS": {
            "init_command": "SET sql_mode='STRICT_TRANS_TABLES'",
            "charset": "utf8mb4",
        }
    }
}

# =====================================================
# PASSWORD VALIDATION
# =====================================================

AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# =====================================================
# INTERNATIONALIZATION
# =====================================================

LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"

USE_I18N = True
USE_TZ = True

# =====================================================
# STATIC FILES
# =====================================================

STATIC_URL = "/static/"

STATIC_ROOT = BASE_DIR / "staticfiles"

STATICFILES_DIRS = [
    BASE_DIR / "static"
]

# WhiteNoise static compression
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# =====================================================
# MEDIA
# =====================================================

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# =====================================================
# DJANGO REST
# =====================================================

REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.AllowAny",
    ],
}

# =====================================================
# CORS
# =====================================================

CORS_ALLOWED_ORIGINS = [
    "https://stevedev.live",
    "https://www.stevedev.live",
    "http://localhost:8080",
]

# =====================================================
# CSRF
# =====================================================

CSRF_TRUSTED_ORIGINS = [
    "http://13.60.83.201",
    "http://13.60.83.201:8000",
    "https://stevedev.live",
    "https://www.stevedev.live",
]

# =====================================================
# SECURITY
# =====================================================

SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True

SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# =====================================================
# LOGGING
# =====================================================

LOG_DIR = BASE_DIR / "logs"

if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "file": {
            "level": "ERROR",
            "class": "logging.FileHandler",
            "filename": LOG_DIR / "django_errors.log",
        },
    },
    "loggers": {
        "django": {
            "handlers": ["file"],
            "level": "ERROR",
            "propagate": True,
        },
    },
}

# =====================================================
# JAZZMIN ADMIN
# =====================================================

JAZZMIN_SETTINGS = {

    "site_title": "SteveDev Backend",

    "site_header": "SteveDev Admin",

    "site_brand": "SteveDev",

    "welcome_sign": "Welcome to SteveDev Backend",

    "copyright": "stevedev.live",

    "site_logo": "logo.png",

    "login_logo": "logo.png",

    "show_sidebar": True,

    "navigation_expanded": True,

    "topmenu_links": [
        {"name": "Portfolio", "url": "https://stevedev.live", "new_window": True},
    ],
}

JAZZMIN_UI_TWEAKS = {
    "theme": "darkly",
    "dark_mode_theme": "darkly",
}

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"