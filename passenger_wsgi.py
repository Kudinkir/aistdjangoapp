# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, '/var/www/u0800358/data/www/kkudinov.ru/aistproject')
sys.path.insert(1, '/var/www/u0800358/data/www/myvenv/lib/python3.7/site-packages')
os.environ['DJANGO_SETTINGS_MODULE'] = 'aistproject.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

