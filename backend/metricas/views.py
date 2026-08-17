from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import MetricaPublicacionForm
from .models import MetricaPublicacion


@login_required
def lista_metricas(request):

    metricas = MetricaPublicacion.objects.select_related(
        "publicacion"
    ).order_by("-fecha_medicion")

    return render(
        request,
        "metricas/lista.html",
        {
            "metricas": metricas,
        },
    )


@login_required
def crear_metrica(request):

    if request.method == "POST":
        form = MetricaPublicacionForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect("metricas:lista")

    else:
        form = MetricaPublicacionForm()

    return render(
        request,
        "metricas/formulario.html",
        {
            "form": form,
        },
    )