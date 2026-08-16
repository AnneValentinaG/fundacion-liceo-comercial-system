from django.urls import path

from . import views


app_name = "contratos"


urlpatterns = [
    path(
        "",
        views.lista_contratos,
        name="lista",
    ),

    path(
        "nuevo/",
        views.crear_contrato,
        name="crear",
    ),

    path(
        "<int:pk>/",
        views.detalle_contrato,
        name="detalle",
    ),
]