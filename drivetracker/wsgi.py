"""
WSGI config for drivetracker project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise

if 'DATABASE_URL' in os.environ:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "drivetracker.settings.heroku")
else:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "drivetracker.settings.local")

application = get_wsgi_application()
application = DjangoWhiteNoise(application)
