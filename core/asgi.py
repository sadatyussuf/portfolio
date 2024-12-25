import os

from django.core.asgi import get_asgi_application

from .base import DEBUG

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
if DEBUG:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.dev")
else:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.prod")

application = get_asgi_application()
