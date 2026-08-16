from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import DocumentoForm
from .models import Documento


@login_required
def lista_documentos(request):

    documentos = Documento.objects.all().order_by("-fecha_registro")

    return render(
        request,
        "documentos/lista.html",
        {
            "documentos": documentos,
        },
    )


@login_required
def crear_documento(request):

    if request.method == "POST":
        form = DocumentoForm(
            request.POST,
            request.FILES,
        )

        if form.is_valid():
            documento = form.save(commit=False)
            documento.creado_por = request.user
            documento.save()

            return redirect("documentos:lista")

    else:
        form = DocumentoForm()

    return render(
        request,
        "documentos/formulario.html",
        {
            "form": form,
        },
    )


@login_required
def detalle_documento(request, pk):

    documento = get_object_or_404(
        Documento,
        pk=pk,
    )

    return render(
        request,
        "documentos/detalle.html",
        {
            "documento": documento,
        },
    )