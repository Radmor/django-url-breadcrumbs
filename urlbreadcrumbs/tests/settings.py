#!/usr/bin/env python
from django.conf import global_settings

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}
INSTALLED_APPS = (
    'django.contrib.contenttypes',
    'django.contrib.auth',
    'urlbreadcrumbs',
    'urlbreadcrumbs.tests',
)
SITE_ID = 1
SECRET_KEY = 'super-secret'
ROOT_URLCONF = 'urlbreadcrumbs.tests.urls'

TEMPLATE_CONTEXT_PROCESSORS = \
    list(global_settings.TEMPLATE_CONTEXT_PROCESSORS) + \
    ['django.core.context_processors.request',  # for ``render_breadcrumbs`` templatetag
     'urlbreadcrumbs.context_processors.build_breadcrumbs']

URLBREADCRUMBS_NAME_MAPPING = {
    'index'  : 'A title for a home page',
    't1home' : 'Index page of Test1',
    'test1ns:t1home' : 'Index page for namespace version of Test1',
    'test1ns:t1aaa_pk' : 'Example of a detail view',
    'test1ns:t1bbb_pk' : 'Example of a detail view with pk: {{ pk }}',
    't1ddd_pk' : 'Example of a detail view without a trailing slash with pk: {{ pk }}',
}
