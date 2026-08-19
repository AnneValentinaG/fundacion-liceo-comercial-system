from django.contrib.auth.models import User
from django.db import models
from django.db.models import Max


class Comunicacion(models.Model):

    class TipoComunicacion(models.TextChoices):
        RECIBIDA = "RECIBIDA", "Recibida"
        ENVIADA = "ENVIADA", "Enviada"

    class EstadoComunicacion(models.TextChoices):
        PENDIENTE = "PENDIENTE", "Pendiente"
        EN_TRAMITE = "EN_TRAMITE", "En trámite"
        RESPONDIDA = "RESPONDIDA", "Respondida"
        CERRADA = "CERRADA", "Cerrada"

    # Número proveniente del Excel
    item = models.PositiveIntegerField(
        unique=True,
        null=True,
        blank=True,
        editable=False,
    )

    numero_radicado = models.CharField(
        max_length=50,
        unique=True,
    )

    tipo = models.CharField(
        max_length=10,
        choices=TipoComunicacion.choices,
        default=TipoComunicacion.RECIBIDA,
    )

    fecha_recibido = models.DateField(
        null=True,
        blank=True,
    )

    hora_recibido = models.TimeField(
        null=True,
        blank=True,
    )

    asunto = models.CharField(
        max_length=250,
    )

    remitente = models.CharField(
        max_length=200,
    )

    # Responsable escrito en el Excel
    responsable_texto = models.CharField(
        max_length=200,
        blank=True,
    )

    # Responsable que existe como usuario Django
    responsable = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="comunicaciones_asignadas",
    )

    dependencia = models.CharField(
        max_length=200,
        blank=True,
    )

    estado_inicial = models.CharField(
        max_length=100,
        blank=True,
    )

    enviado_a = models.CharField(
        max_length=200,
        blank=True,
    )

    fecha_asignacion = models.DateField(
        null=True,
        blank=True,
    )

    hora_asignacion = models.TimeField(
        null=True,
        blank=True,
    )

    termino_dias = models.PositiveIntegerField(
        null=True,
        blank=True,
    )

    estado = models.CharField(
        max_length=20,
        choices=EstadoComunicacion.choices,
        default=EstadoComunicacion.PENDIENTE,
    )

    estado_actual_texto = models.CharField(
        max_length=100,
        blank=True,
    )

    observaciones = models.TextField(
        blank=True,
    )

    # Permite indicar que esta comunicación
    # es respuesta de otra.
    respuesta_a = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="respuestas",
    )

    archivo = models.FileField(
        upload_to="comunicaciones/%Y/%m/",
        null=True,
        blank=True,
    )

    fecha_registro = models.DateTimeField(
        auto_now_add=True,
    )

    fecha_actualizacion = models.DateTimeField(
        auto_now=True,
    )

    def save(self, *args, **kwargs):

        if self.item is None:

            ultimo_item = (
                Comunicacion.objects.aggregate(
                    max_item=Max("item")
                )["max_item"]
                or 0
            )

            self.item = ultimo_item + 1

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.numero_radicado} - {self.asunto}"