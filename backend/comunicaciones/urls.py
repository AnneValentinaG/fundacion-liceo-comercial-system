from django.urls import path

from . import views


app_name = "comunicaciones"


urlpatterns = [

    path(
        "",
        views.lista_comunicaciones,
        name="lista",
    ),

    path(
        "nueva/",
        views.crear_comunicacion,
        name="crear",
    ),

    path(
        "<int:pk>/editar/",
        views.editar_comunicacion,
        name="editar",
    ),

    path(
        "<int:pk>/",
        views.detalle_comunicacion,
        name="detalle",
    ),

    path(
        "importar/",
        views.importar_excel,
        name="importar",
    ),
]