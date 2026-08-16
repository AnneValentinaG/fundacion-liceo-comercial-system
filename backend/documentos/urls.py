from django.urls import path

from . import views


app_name = "documentos"


urlpatterns = [
    path(
        "",
        views.lista_documentos,
        name="lista",
    ),

    path(
        "nuevo/",
        views.crear_documento,
        name="crear",
    ),

    path(
        "<int:pk>/",
        views.detalle_documento,
        name="detalle",
    ),
]