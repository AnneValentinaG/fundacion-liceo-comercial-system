from django.contrib.auth.models import User
from django.db import models


class Documento(models.Model):

    class TipoDocumento(models.TextChoices):
        ENTRADA = "ENTRADA", "Entrada"
        SALIDA = "SALIDA", "Salida"
        INTERNO = "INTERNO", "Interno"

    class EstadoDocumento(models.TextChoices):
        RECIBIDO = "RECIBIDO", "Recibido"
        ASIGNADO = "ASIGNADO", "Asignado"
        EN_TRAMITE = "EN_TRAMITE", "En trámite"
        RESPONDIDO = "RESPONDIDO", "Respondido"
        ARCHIVADO = "ARCHIVADO", "Archivado"

    numero_radicado = models.CharField(
        max_length=50,
        unique=True,
    )

    fecha_documento = models.DateField()

    remitente = models.CharField(
        max_length=150,
    )

    asunto = models.CharField(
        max_length=255,
    )

    tipo = models.CharField(
        max_length=20,
        choices=TipoDocumento.choices,
        default=TipoDocumento.ENTRADA,
    )

    estado = models.CharField(
        max_length=20,
        choices=EstadoDocumento.choices,
        default=EstadoDocumento.RECIBIDO,
    )

    responsable = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="documentos_asignados",
    )

    archivo = models.FileField(
        upload_to="documentos/%Y/%m/",
        null=True,
        blank=True,
    )

    observaciones = models.TextField(
        blank=True,
    )

    fecha_registro = models.DateTimeField(
        auto_now_add=True,
    )

    fecha_actualizacion = models.DateTimeField(
        auto_now=True,
    )

    def __str__(self):
        return f"{self.numero_radicado} - {self.asunto}"