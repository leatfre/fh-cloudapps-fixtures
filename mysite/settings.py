import os

import dj_database_url

SECRET_KEY = os.environ.get("SECRET_KEY", "fixture-only-not-secret")
DEBUG = False
ALLOWED_HOSTS = ["*"]
INSTALLED_APPS = ["django.contrib.contenttypes", "django.contrib.auth"]
MIDDLEWARE = []
ROOT_URLCONF = "mysite.urls"
WSGI_APPLICATION = "mysite.wsgi.application"
DATABASES = {"default": dj_database_url.config(conn_max_age=60)}
USE_TZ = True
