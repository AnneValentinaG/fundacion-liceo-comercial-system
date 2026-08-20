import os

from django.core.wsgi import get_wsgi_application


os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    "config.settings",
)

application = get_wsgi_application()


from core.create_superuser import create_superuser_if_needed

create_superuser_if_needed()