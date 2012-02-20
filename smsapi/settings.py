# -*- encoding: utf-8 -*-

from django.conf import settings

try:
    SMSAPI_USERNAME = getattr(settings, 'SMSAPI_USERNAME')
except AttributeError:
    raise BaseException('Atrybut SMSAPI_USERNAME wymagany')

try:
    SMSAPI_PASSWORD = getattr(settings, 'SMSAPI_PASSWORD')
except AttributeError:
    raise BaseException('Atrybut SMSAPI_PASSWORD wymagany')

try:
    SMSAPI_TEST_EMAIL = getattr(settings, 'SMSAPI_TEST_EMAIL')
except AttributeError:
    raise BaseException('Atrybut SMSAPI_TEST_EMAIL wymagany')
