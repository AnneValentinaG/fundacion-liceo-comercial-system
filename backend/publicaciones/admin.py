from django.contrib import admin

from .models import Publicacion


@admin.register(Publicacion)
class PublicacionAdmin(admin.ModelAdmin):
    list_display = (
        "tema",
        "red_social",
        "estado",
        "fecha_publicacion",
    )

    list_filter = (
        "red_social",
        "estado",
    )

    search_fields = (
        "tema",
        "contenido",
    )