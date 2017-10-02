# -*- coding: utf-8 -*-

from django.conf import settings

import os


MAINTENANCE_MODE = getattr(
    settings, 'MAINTENANCE_MODE', False)
MAINTENANCE_MODE_GET_CLIENT_IP_ADDRESS = getattr(
    settings, 'MAINTENANCE_MODE_GET_CLIENT_IP_ADDRESS', None)
MAINTENANCE_MODE_GET_TEMPLATE_CONTEXT = getattr(
    settings, 'MAINTENANCE_MODE_GET_TEMPLATE_CONTEXT', None)
MAINTENANCE_MODE_IGNORE_IP_ADDRESSES = getattr(
    settings, 'MAINTENANCE_MODE_IGNORE_IP_ADDRESSES', None)
MAINTENANCE_MODE_IGNORE_STAFF = getattr(
    settings, 'MAINTENANCE_MODE_IGNORE_STAFF', False)
MAINTENANCE_MODE_IGNORE_SUPERUSER = getattr(
    settings, 'MAINTENANCE_MODE_IGNORE_SUPERUSER', False)
MAINTENANCE_MODE_IGNORE_TESTS = getattr(
    settings, 'MAINTENANCE_MODE_IGNORE_TESTS', False)
MAINTENANCE_MODE_IGNORE_URLS = getattr(
    settings, 'MAINTENANCE_MODE_IGNORE_URLS', None)
MAINTENANCE_MODE_REDIRECT_URL = getattr(
    settings, 'MAINTENANCE_MODE_REDIRECT_URL', None)
MAINTENANCE_MODE_STATE_FILE_PATH = getattr(
    settings, 'MAINTENANCE_MODE_STATE_FILE_PATH',
    os.path.join(os.path.abspath(
        os.path.dirname(__file__)), 'maintenance_mode_state.txt'))
MAINTENANCE_MODE_TEMPLATE = getattr(
    settings, 'MAINTENANCE_MODE_TEMPLATE', '503.html')
