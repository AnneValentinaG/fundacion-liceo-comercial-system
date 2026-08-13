from django.contrib import admin

from .models import MetricaPublicacion


@admin.register(MetricaPublicacion)
class MetricaPublicacionAdmin(admin.ModelAdmin):

    list_display = (
        "publicacion",
        "alcance",
        "total_interacciones",
        "tasa_interaccion",
        "fecha_medicion",
    )