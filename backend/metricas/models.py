from django.db import models

from publicaciones.models import Publicacion


class MetricaPublicacion(models.Model):

    publicacion = models.ForeignKey(
        Publicacion,
        on_delete=models.CASCADE,
        related_name="metricas",
    )

    alcance = models.PositiveIntegerField(
        default=0,
    )

    reacciones = models.PositiveIntegerField(
        default=0,
    )

    comentarios = models.PositiveIntegerField(
        default=0,
    )

    compartidos = models.PositiveIntegerField(
        default=0,
    )

    guardados = models.PositiveIntegerField(
        default=0,
    )

    impresiones = models.PositiveIntegerField(
        default=0,
    )

    fecha_medicion = models.DateTimeField(
        auto_now_add=True,
    )

    @property
    def total_interacciones(self):
        return (
            self.reacciones
            + self.comentarios
            + self.compartidos
            + self.guardados
        )

    @property
    def tasa_interaccion(self):
        if self.alcance == 0:
            return 0

        return round(
            (self.total_interacciones / self.alcance) * 100,
            2,
        )

    def __str__(self):
        return f"Métricas - {self.publicacion}"