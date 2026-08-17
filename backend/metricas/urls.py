from django.urls import path

from . import views


app_name = "metricas"


urlpatterns = [
    path(
        "",
        views.lista_metricas,
        name="lista",
    ),

    path(
        "nueva/",
        views.crear_metrica,
        name="crear",
    ),
]