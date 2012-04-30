#-*- coding: utf-8 -*-

SMSAPI_URL = 'http://api.smsapi.pl/sms.do'
SMSAPI_URL_BACKUP = 'http://api2.smsapi.pl/sms.do'
SMSAPI_SSL_URL = 'https://ssl.smsapi.pl/sms.do'
SMSAPI_SSL_URL_BACKUP = 'https://ssl2.smsapi.pl/sms.do'

import urllib, hashlib
from smsapi.settings import SMSAPI_USERNAME, SMSAPI_PASSWORD, SMSAPI_TEST_EMAIL
from django.core.mail import send_mail

def sendSMS(message, toNumber, fromNumber = '', useSSL = False, flash = 0, encoding = 'windows-1250', details = 0, date = None, datacoding = False, idx = None, single = 0, nounicode = 0, fast = 0, test = False, test_email = SMSAPI_TEST_EMAIL):
    
    params = {
        'username': SMSAPI_USERNAME,
        'password': hashlib.md5(SMSAPI_PASSWORD).hexdigest(),
        'to': toNumber,
        'from': fromNumber,
        'message': message,
        'encoding': encoding,
        'flash': flash,
        'details': details,
        'date': date,
        'idx': idx,
        'single': single,
        'nounicode': nounicode,
        'fast': 0,
    }

    if test:
        params.update({'test': 1})

        send_mail('TEST smsapi.pl', message, test_email, [test_email])

    if datacoding:
        params.update({'datacoding': 'bin'})

    params = urllib.urlencode(params)

    if useSSL:
        servers = [SMSAPI_SSL_URL, SMSAPI_SSL_URL_BACKUP]
    else:
        servers = [SMSAPI_URL, SMSAPI_URL_BACKUP]

    for server in servers:
        try:
            urlHandler = urllib.urlopen(server, params)
        except:
            if server == servers[-1]:
                raise

            continue

        content = urlHandler.read()
        urlHandler.close()

        if content.startswith('OK'):
            status, smsId, points = content.split(':')
            return {'status': status, 'smsId': smsId, 'points': points}
        else:
            status, errorNumber = content.split(':')
            return {'status': status, 'errorNumber': errorNumber}
