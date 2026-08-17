from django import forms

from .models import MetricaPublicacion


class MetricaPublicacionForm(forms.ModelForm):

    class Meta:
        model = MetricaPublicacion

        fields = [
            "publicacion",
            "alcance",
            "reacciones",
            "comentarios",
            "compartidos",
            "guardados",
            "impresiones",
        ]