from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ContratoForm
from .models import Contrato


@login_required
def lista_contratos(request):
    contratos = Contrato.objects.all().order_by("-fecha_registro")

    return render(
        request,
        "contratos/lista.html",
        {
            "contratos": contratos,
        },
    )


@login_required
def crear_contrato(request):

    if request.method == "POST":
        form = ContratoForm(
            request.POST,
            request.FILES,
        )

        if form.is_valid():
            form.save()
            return redirect("contratos:lista")

    else:
        form = ContratoForm()

    return render(
        request,
        "contratos/formulario.html",
        {
            "form": form,
        },
    )


@login_required
def detalle_contrato(request, pk):
    contrato = get_object_or_404(
        Contrato,
        pk=pk,
    )

    return render(
        request,
        "contratos/detalle.html",
        {
            "contrato": contrato,
        },
    )