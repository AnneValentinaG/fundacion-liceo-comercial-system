from django.urls import path

from . import views


app_name = "publicaciones"


urlpatterns = [
    path(
        "",
        views.lista_publicaciones,
        name="lista",
    ),

    path(
        "nueva/",
        views.crear_publicacion,
        name="crear",
    ),

    path(
        "<int:pk>/",
        views.detalle_publicacion,
        name="detalle",
    ),
]