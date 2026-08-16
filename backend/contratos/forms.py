from django import forms

from .models import Contrato


class ContratoForm(forms.ModelForm):

    class Meta:
        model = Contrato

        fields = [
            "numero_contrato",
            "contratista",
            "objeto",
            "tipo_contrato",
            "fecha_firma",
            "fecha_inicio",
            "fecha_fin",
            "valor",
            "estado",
            "responsable",
            "archivo_principal",
            "observaciones",
        ]

        widgets = {
            "fecha_firma": forms.DateInput(attrs={"type": "date"}),
            "fecha_inicio": forms.DateInput(attrs={"type": "date"}),
            "fecha_fin": forms.DateInput(attrs={"type": "date"}),
            "objeto": forms.Textarea(attrs={"rows": 4}),
            "observaciones": forms.Textarea(attrs={"rows": 4}),
        }