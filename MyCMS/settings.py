import os  # isort:skip
gettext = lambda s: s
DATA_DIR = os.path.dirname(os.path.dirname(__file__))
"""
Django settings for MyCMS project.

Generated by 'django-admin startproject' using Django 1.11.22.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '2eni8l^y6d-bpu0$4gm7sj=8%y5qb5v_0lp=%5ox6b7b--ny_z'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost', '.sipco-france.fr', 'sipcofrance.pythonanywhere.com']


# Application definition





ROOT_URLCONF = 'MyCMS.urls'




# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'fr'

TIME_ZONE = 'Europe/Paris'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(DATA_DIR, 'media')
STATIC_ROOT = os.path.join(DATA_DIR, 'static')

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'MyCMS', 'static'),
)

SITE_ID = 1


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'MyCMS', 'templates'),],
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.i18n',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.media',
                'django.template.context_processors.csrf',
                'django.template.context_processors.tz',
                'sekizai.context_processors.sekizai',
                'django.template.context_processors.static',
                'cms.context_processors.cms_settings'
            ],
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
                'django.template.loaders.eggs.Loader',
            ],
        },
    },
]


MIDDLEWARE = [
    'cms.middleware.utils.ApphookReloadMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware',
]

INSTALLED_APPS = [
    'djangocms_admin_style',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.admin',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'django.contrib.staticfiles',
    'django.contrib.messages',
    'cms',
    'menus',
    'sekizai',
    'treebeard',
    'djangocms_text_ckeditor',
    'easy_thumbnails',
    'filer',
    'mptt',
    'djangocms_column',
    'djangocms_style',
    'djangocms_snippet',
    'djangocms_googlemap',
    'djangocms_video',
    'aldryn_bootstrap3',
    'cmsplugin_css_background',
    'MyCMS'
]

LANGUAGES = (
    ## Customize this
    ('en', gettext('en')),
    ('fr', gettext('fr')),
    ('es', gettext('es')),
)

CMS_LANGUAGES = {
    ## Customize this
    1: [
        {
            'code': 'en',
            'name': gettext('en'),
            'redirect_on_fallback': True,
            'public': True,
            'hide_untranslated': False,
        },
        {
            'code': 'fr',
            'name': gettext('fr'),
            'redirect_on_fallback': True,
            'public': True,
            'hide_untranslated': False,
        },
        {
            'code': 'es',
            'name': gettext('es'),
            'redirect_on_fallback': True,
            'public': True,
            'hide_untranslated': False,
        },
    ],
    'default': {
        'redirect_on_fallback': True,
        'public': True,
        'hide_untranslated': False,
    },
}

CMS_TEMPLATES = (
    ## Customize this
    ('fullwidth.html', 'Fullwidth'),
    ('home.html', 'Home')
)

CMS_PERMISSION = True

CMS_PLACEHOLDER_CONF = {
        'element_background_image': {
            'plugins': ['CssBackgroundPlugin'],
            'limits': {
                'global': 1,
            },
        },
}


DATABASES = {
    'default': {
        'CONN_MAX_AGE': 0,
        'ENGINE': 'django.db.backends.sqlite3',
        'HOST': 'localhost',
        'NAME': 'project.db',
        'PASSWORD': '',
        'PORT': '',
        'USER': ''
    }
}

MIGRATION_MODULES = {
    
}

THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters'
)


## ALDRYN COMPONENTS

#ALDRYN_BOOTSTRAP3_CAROUSEL_STYLES = [
#    ('feature', _('Featured Version')),
#]

ALDRYN_BOOTSTRAP3_ICONSETS = [
    ('glyphicons', 'glyphicons', 'Glyphicons'),
    ('fontawesome', 'fa', 'Font Awesome'),
    # custom iconsets have to be JSON
    ('{"iconClass": "icon", "iconClassFix": "icon-", "icons": [...]}', 'icon', 'Custom Font Icons'),
    ('{"svg": true, "spritePath": "sprites/icons.svg", "iconClass": "icon", "iconClassFix": "icon-", "icons": [...]}', 'icon', 'Custom SVG Icons'),
]

ALDRYN_BOOTSTRAP3_GRID_SIZE = 12

CKEDITOR_SETTINGS = {
    'stylesSet': [
        {
            'name': 'Page Header H1',
            'element': 'h1',
            'attributes': {
                'class': 'page-header',
            }
        },
        {
            'name': 'Page Header H2',
            'element': 'h2',
            'attributes': {
                'class': 'page-header',
            }
        },
        {
            'name': 'Page Header H3',
            'element': 'h3',
            'attributes': {
                'class': 'page-header',
            }
        },
        {
            'name': 'Code',
            'element': 'code',
        },
        {
            'name': 'Code Block',
            'element': 'pre',
            'attributes': {
                'class': 'code',
            }
        },
    ]
}