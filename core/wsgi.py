import os

from django.core.wsgi import get_wsgi_application

from .base import DEBUG


# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
if DEBUG:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.dev")
else:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.prod")

application = get_wsgi_application()
