from decimal import Decimal

from django.contrib.auth.models import User
from django.db import models


class Contrato(models.Model):

    class EstadoContrato(models.TextChoices):
        PLANEADO = "PLANEADO", "Planeado"
        EJECUCION = "EJECUCION", "En ejecución"
        SUSPENDIDO = "SUSPENDIDO", "Suspendido"
        FINALIZADO = "FINALIZADO", "Finalizado"
        LIQUIDADO = "LIQUIDADO", "Liquidado"

    class TipoContrato(models.TextChoices):
        PRESTACION_SERVICIOS = "PRESTACION_SERVICIOS", "Prestación de servicios"
        SUMINISTRO = "SUMINISTRO", "Suministro"
        COMPRAVENTA = "COMPRAVENTA", "Compraventa"
        ARRENDAMIENTO = "ARRENDAMIENTO", "Arrendamiento"
        CONVENIO = "CONVENIO", "Convenio"
        OTRO = "OTRO", "Otro"

    numero_contrato = models.CharField(
        max_length=50,
        unique=True,
    )

    contratista = models.CharField(
        max_length=200,
    )

    objeto = models.TextField()

    tipo_contrato = models.CharField(
        max_length=30,
        choices=TipoContrato.choices,
        default=TipoContrato.OTRO,
    )

    fecha_firma = models.DateField(
        null=True,
        blank=True,
    )

    fecha_inicio = models.DateField()

    fecha_fin = models.DateField()

    valor = models.DecimalField(
        max_digits=15,
        decimal_places=2,
        default=Decimal("0.00"),
    )

    estado = models.CharField(
        max_length=20,
        choices=EstadoContrato.choices,
        default=EstadoContrato.PLANEADO,
    )

    responsable = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="contratos_asignados",
    )

    archivo_principal = models.FileField(
        upload_to="contratos/principales/%Y/%m/",
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
        return f"{self.numero_contrato} - {self.contratista}"


class DocumentoContrato(models.Model):

    contrato = models.ForeignKey(
        Contrato,
        on_delete=models.CASCADE,
        related_name="documentos",
    )

    nombre = models.CharField(
        max_length=150,
    )

    archivo = models.FileField(
        upload_to="contratos/documentos/%Y/%m/",
    )

    fecha_carga = models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self):
        return f"{self.contrato.numero_contrato} - {self.nombre}"