from django import forms

from .models import Publicacion


class PublicacionForm(forms.ModelForm):

    class Meta:
        model = Publicacion

        fields = [
            "red_social",
            "fecha_publicacion",
            "tema",
            "contenido",
            "tipo_contenido",
            "enlace_publicacion",
            "estado",
        ]

        widgets = {
            "fecha_publicacion": forms.DateTimeInput(
                attrs={"type": "datetime-local"}
            ),
            "contenido": forms.Textarea(
                attrs={"rows": 6}
            ),
        }