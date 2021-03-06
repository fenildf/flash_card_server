# -*- coding: utf-8 -*-
"""
Django settings for day365_server project.

Generated by 'django-admin startproject' using Django 1.8.7.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'r59r2s_s6o=1r_9--dndv-kz@1d(*0fqpsf^u0v%rxorm7i^m='

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'lite',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'lite.lib.middleware.SessionMiddleware'
)

ROOT_URLCONF = 'flash_card_server.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
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

WSGI_APPLICATION = 'flash_card_server.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    # }
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'flash_card',
        'USER': 'root',
        'PASSWORD':'root',
        'HOST':'127.0.0.1',
        'PORT':'3306',
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'zh_CN'
TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

# USE_TZ = True
USE_TZ = False #计算机所在地时间#

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "static")


APP_ID = "wx95ed67937837f4e5"
APP_SECRET = "a3f103b09e27d46b722aa2e74afb39be"
MACH_ID = "1488713872"
MACH_KEY = "283fc3d9d4b8ba3b58601145466d4417"

# 七牛配置
QINIU_ACCESS_KEY = 'bK5xWj0a-TBIljlxHYOHuQib9HYF_9Ft-HtP8tEb'
QINIU_SECRET_KEY = '56lucORYc45sF5eDqNk63mLXsQ78n4RrubIrjtE0'
QINIU_BUCKET_NAME = 'clickz'
QINIU_HOST = 'http://image.12xiong.top/'
QINIU_CALLBACK_URL = "https://www.12xiong.top/day365/lite/upload/callback/"
QINIU_CALLBACK_BODY = "key=$(key)&hash=$(etag)&w=$(imageInfo.width)&h=$(imageInfo.height)&duration=$(avinfo.video.duration)&fsize=$(fsize)&vw=$(avinfo.video.width)&vh=$(avinfo.video.height)"
QINIU_CALLBACK_HOST = "120.27.97.33"
QINIU_FSIZE_LIMIT = 6815744















