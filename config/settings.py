"""Minimal Django settings for the DayZer0 catalog starter.

This is a deliberately small, generic skeleton: one health app, DRF installed,
no database models of your own yet. Build your project's feature on top of it.
"""
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# Dev-only key. Set DJANGO_SECRET_KEY in the environment for anything real.
import os

SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY", "dev-only-not-a-secret")
DEBUG = os.environ.get("DJANGO_DEBUG", "1") == "1"
ALLOWED_HOSTS = ["*"]

INSTALLED_APPS = [
    "django.contrib.contenttypes",
    "django.contrib.auth",
    "rest_framework",
    "health",
]

MIDDLEWARE = [
    "django.middleware.common.CommonMiddleware",
]

ROOT_URLCONF = "config.urls"
WSGI_APPLICATION = "config.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

USE_TZ = True
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
