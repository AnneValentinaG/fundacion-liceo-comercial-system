from django.contrib import admin

from .models import Documento


@admin.register(Documento)
class DocumentoAdmin(admin.ModelAdmin):
    list_display = (
        "numero_radicado",
        "fecha_documento",
        "remitente",
        "tipo",
        "estado",
        "responsable",
    )

    list_filter = (
        "tipo",
        "estado",
    )

    search_fields = (
        "numero_radicado",
        "remitente",
        "asunto",
    )