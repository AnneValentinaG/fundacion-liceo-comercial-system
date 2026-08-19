from django import forms

from .models import Comunicacion


class ComunicacionForm(forms.ModelForm):

    class Meta:
        model = Comunicacion

        fields = [
            
            "numero_radicado",
            "tipo",
            "fecha_recibido",
            "hora_recibido",
            "asunto",
            "remitente",
            "responsable_texto",
            "responsable",
            "dependencia",
            "estado_inicial",
            "enviado_a",
            "fecha_asignacion",
            "hora_asignacion",
            "termino_dias",
            "estado",
            "estado_actual_texto",
            "respuesta_a",
            "archivo",
            "observaciones",
        ]

        widgets = {

            "fecha_recibido": forms.DateInput(
                format="%Y-%m-%d",
                attrs={
                    "type": "date",
                }
            ),

            "hora_recibido": forms.TimeInput(
                format="%H:%M",
                attrs={
                    "type": "time",
                }
            ),

            "fecha_asignacion": forms.DateInput(
                format="%Y-%m-%d",
                attrs={
                    "type": "date",
                }
            ),

            "hora_asignacion": forms.TimeInput(
                format="%H:%M",
                attrs={
                    "type": "time",
                }
            ),

            "observaciones": forms.Textarea(
                attrs={
                    "rows": 4,
                }
            ),
        }

        labels = {

            

            "numero_radicado": "Número de radicado",

            "tipo": "Tipo de comunicación",

            "fecha_recibido": "Fecha recibido",

            "hora_recibido": "Hora recibido",

            "asunto": "Asunto",

            "remitente": "Remitente",

            "responsable_texto": "Responsable registrado",

            "responsable": "Usuario responsable",

            "dependencia": "Dependencia",

            "estado_inicial": "Estado inicial",

            "enviado_a": "Enviado a",

            "fecha_asignacion": "Fecha de asignación",

            "hora_asignacion": "Hora de asignación",

            "termino_dias": "Término en días",

            "estado": "Estado del sistema",

            "estado_actual_texto": "Estado actual",

            "respuesta_a": "¿Esta comunicación responde a otra?",

            "archivo": "Archivo asociado",

            "observaciones": "Observaciones",
        }

        input_formats = {
            "fecha_recibido": ["%Y-%m-%d"],
            "fecha_asignacion": ["%Y-%m-%d"],
            "hora_recibido": ["%H:%M", "%H:%M:%S"],
            "hora_asignacion": ["%H:%M", "%H:%M:%S"],
        }


class ImportarComunicacionesForm(forms.Form):

    archivo_excel = forms.FileField(
        label="Archivo Excel",
        help_text=(
            "Selecciona el archivo .xlsx con el "
            "seguimiento de comunicaciones."
        ),
    )

    def clean_archivo_excel(self):

        archivo = self.cleaned_data["archivo_excel"]

        if not archivo.name.lower().endswith(".xlsx"):

            raise forms.ValidationError(
                "El archivo debe estar en formato .xlsx."
            )

        return archivo