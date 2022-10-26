"""
WSGI config for BookStore project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import sys
import os
sys.path.append("/home/ubuntu/Radha-Damodar/BookStore")
sys.path.append("/home/ubuntu/Radha-Damodar/BookStore/BookStore")
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'BookStore.settings')

application = get_wsgi_application()
