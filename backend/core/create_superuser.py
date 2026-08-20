import os

from django.contrib.auth import get_user_model


def create_superuser_if_needed():

    username = os.getenv("SUPERUSER_USERNAME")
    email = os.getenv("SUPERUSER_EMAIL")
    password = os.getenv("SUPERUSER_PASSWORD")

    if not username or not password:
        return

    User = get_user_model()

    if not User.objects.filter(username=username).exists():

        User.objects.create_superuser(
            username=username,
            email=email or "",
            password=password,
        )

        print("Superusuario creado correctamente.")

    else:
        print("El superusuario ya existe.")