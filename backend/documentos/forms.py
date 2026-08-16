from django import forms

from .models import Documento


class DocumentoForm(forms.ModelForm):

    class Meta:
        model = Documento

        fields = [
            "numero_radicado",
            "fecha_documento",
            "fecha_recepcion",
            "remitente",
            "destinatario",
            "dependencia",
            "asunto",
            "tipo",
            "estado",
            "responsable",
            "archivo",
            "observaciones",
        ]

        widgets = {
            "fecha_documento": forms.DateInput(
                attrs={"type": "date"}
            ),
            "fecha_recepcion": forms.DateInput(
                attrs={"type": "date"}
            ),
            "observaciones": forms.Textarea(
                attrs={"rows": 4}
            ),
        }