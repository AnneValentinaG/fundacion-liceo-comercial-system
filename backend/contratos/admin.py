from django.contrib import admin

from .models import Contrato, DocumentoContrato


@admin.register(Contrato)
class ContratoAdmin(admin.ModelAdmin):
    list_display = (
        "numero_contrato",
        "contratista",
        "fecha_inicio",
        "fecha_fin",
        "estado",
        "valor",
    )

    list_filter = (
        "estado",
    )

    search_fields = (
        "numero_contrato",
        "contratista",
        "objeto",
    )


admin.site.register(DocumentoContrato)