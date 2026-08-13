from django.contrib import admin

from .models import PerfilUsuario


@admin.register(PerfilUsuario)
class PerfilUsuarioAdmin(admin.ModelAdmin):
    list_display = (
        "identificacion",
        "usuario",
        "telefono",
        "fecha_creacion",
    )

    search_fields = (
        "identificacion",
        "usuario__username",
        "usuario__first_name",
        "usuario__last_name",
    )