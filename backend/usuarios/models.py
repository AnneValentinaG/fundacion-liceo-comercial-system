from django.contrib.auth.models import User
from django.db import models


class PerfilUsuario(models.Model):
    usuario = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="perfil",
    )

    identificacion = models.CharField(
        max_length=30,
        unique=True,
    )

    fecha_nacimiento = models.DateField(
        null=True,
        blank=True,
    )

    telefono = models.CharField(
        max_length=30,
        blank=True,
    )

    fecha_creacion = models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self):
        return f"{self.usuario.get_full_name()} - {self.identificacion}"



    