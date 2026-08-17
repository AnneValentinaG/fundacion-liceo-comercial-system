from django import forms


class AsistenteContenidoForm(forms.Form):

    REDES = [
        ("FACEBOOK", "Facebook"),
        ("INSTAGRAM", "Instagram"),
        ("GENERAL", "General"),
    ]

    OBJETIVOS = [
        ("INFORMATIVO", "Informativo"),
        ("INVITACION", "Invitación"),
        ("EDUCATIVO", "Educativo"),
        ("RECONOCIMIENTO", "Reconocimiento"),
        ("OTRO", "Otro"),
    ]

    tema = forms.CharField(
        max_length=180,
        label="Tema de la publicación",
    )

    red_social = forms.ChoiceField(
        choices=REDES,
        label="Red social",
    )

    objetivo = forms.ChoiceField(
        choices=OBJETIVOS,
        label="Objetivo",
    )

    descripcion = forms.CharField(
        label="Describe lo que deseas comunicar",
        widget=forms.Textarea(
            attrs={
                "rows": 7,
                "placeholder": (
                    "Ejemplo: Necesito una publicación sobre "
                    "una jornada de capacitación para docentes..."
                ),
            }
        ),
    )