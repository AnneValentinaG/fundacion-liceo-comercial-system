from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import PublicacionForm
from .models import Publicacion


@login_required
def lista_publicaciones(request):

    publicaciones = Publicacion.objects.all().order_by(
        "-fecha_registro"
    )

    return render(
        request,
        "publicaciones/lista.html",
        {
            "publicaciones": publicaciones,
        },
    )


@login_required
def crear_publicacion(request):

    if request.method == "POST":
        form = PublicacionForm(request.POST)

        if form.is_valid():
            publicacion = form.save(commit=False)
            publicacion.creado_por = request.user
            publicacion.save()

            return redirect("publicaciones:lista")

    else:
        form = PublicacionForm()

    return render(
        request,
        "publicaciones/formulario.html",
        {
            "form": form,
        },
    )


@login_required
def detalle_publicacion(request, pk):

    publicacion = get_object_or_404(
        Publicacion,
        pk=pk,
    )

    return render(
        request,
        "publicaciones/detalle.html",
        {
            "publicacion": publicacion,
        },
    )