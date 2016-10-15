"""
WSGI config for blogger project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""
import os
import sys

from django.core.wsgi import get_wsgi_application
path = 'C:\Users\Kurgat\AppData\Local\Programs\Python\Python35\Scripts\blogger'
if path not in sys.path:
    sys.path.append(path)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "blogger.settings")

application = get_wsgi_application()
