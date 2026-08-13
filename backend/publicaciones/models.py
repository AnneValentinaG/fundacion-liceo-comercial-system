from django.contrib.auth.models import User
from django.db import models


class Publicacion(models.Model):

    class RedSocial(models.TextChoices):
        FACEBOOK = "FACEBOOK", "Facebook"
        INSTAGRAM = "INSTAGRAM", "Instagram"
        TIKTOK = "TIKTOK", "TikTok"
        OTRA = "OTRA", "Otra"

    class EstadoPublicacion(models.TextChoices):
        BORRADOR = "BORRADOR", "Borrador"
        PROGRAMADA = "PROGRAMADA", "Programada"
        PUBLICADA = "PUBLICADA", "Publicada"

    red_social = models.CharField(
        max_length=20,
        choices=RedSocial.choices,
    )

    fecha_publicacion = models.DateTimeField(
        null=True,
        blank=True,
    )

    tema = models.CharField(
        max_length=150,
    )

    contenido = models.TextField()

    tipo_contenido = models.CharField(
        max_length=50,
        blank=True,
    )

    estado = models.CharField(
        max_length=20,
        choices=EstadoPublicacion.choices,
        default=EstadoPublicacion.BORRADOR,
    )

    creado_por = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name="publicaciones_creadas",
    )

    fecha_registro = models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self):
        return f"{self.red_social} - {self.tema}"