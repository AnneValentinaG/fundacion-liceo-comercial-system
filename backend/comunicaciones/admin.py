from django.contrib import admin

from .models import Comunicacion


@admin.register(Comunicacion)
class ComunicacionAdmin(admin.ModelAdmin):

    list_display = (
        "numero_radicado",
        "tipo",
        "fecha_recibido",
        "remitente",
        "responsable_texto",
        "dependencia",
        "estado",
    )

    list_filter = (
        "tipo",
        "estado",
        "dependencia",
    )

    search_fields = (
        "numero_radicado",
        "remitente",
        "responsable_texto",
        "dependencia",
        "asunto",
        "enviado_a",
    )

    ordering = (
        "-fecha_recibido",
        "-fecha_registro",
    )