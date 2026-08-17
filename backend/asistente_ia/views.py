from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .forms import AsistenteContenidoForm


def generar_contenido_local(tema, red_social, objetivo, descripcion):

    tema_limpio = tema.strip()
    descripcion_limpia = descripcion.strip()

    # Texto base según objetivo
    textos_objetivo = {
        "INFORMATIVO": (
            f"La Fundación Liceo Comercial Ciudad De El Bordo comparte información "
            f"sobre {tema_limpio}. {descripcion_limpia} "
            f"Continuamos fortaleciendo nuestros procesos institucionales y educativos, "
            f"promoviendo espacios que aporten al crecimiento de nuestra comunidad."
        ),

        "INVITACION": (
            f"La Fundación Liceo Comercial Ciudad De El Bordo invita cordialmente a participar "
            f"en {tema_limpio}. {descripcion_limpia} "
            f"Esperamos contar con su participación y compartir juntos este espacio institucional."
        ),

        "EDUCATIVO": (
            f"En la Fundación Liceo Comercial Ciudad De El Bordo seguimos construyendo espacios "
            f"de aprendizaje alrededor de {tema_limpio}. {descripcion_limpia} "
            f"Estas actividades permiten fortalecer conocimientos, experiencias y oportunidades "
            f"para nuestra comunidad educativa."
        ),

        "RECONOCIMIENTO": (
            f"La Fundación Liceo Comercial Ciudad De El Bordo reconoce y agradece la participación "
            f"en {tema_limpio}. {descripcion_limpia} "
            f"Valoramos el compromiso, disposición y trabajo de todas las personas que hicieron "
            f"posible esta actividad."
        ),

        "OTRO": (
            f"La Fundación Liceo Comercial Ciudad De El Bordo presenta información relacionada con "
            f"{tema_limpio}. {descripcion_limpia} "
            f"Seguimos trabajando por el fortalecimiento de nuestros procesos institucionales."
        ),
    }

    texto = textos_objetivo.get(
        objetivo,
        textos_objetivo["OTRO"]
    )

    # Ajuste sencillo según red social
    if red_social == "INSTAGRAM":
        texto += "\n\n📲 Síguenos para conocer más sobre nuestras actividades y procesos."

    elif red_social == "FACEBOOK":
        texto += "\n\nComparte esta información y acompáñanos en nuestras actividades."

    # Hashtags base
    hashtags = [
        "#FundaciónLiceoComercial",
        "#CiudadDeElBordo",
        "#Educación",
        "#ConstruyendoFuturo",
    ]

    tema_lower = tema_limpio.lower()

    if "docente" in tema_lower or "capacitación" in tema_lower:
        hashtags.extend([
            "#FormaciónDocente",
            "#Capacitación",
        ])

    if "estudiante" in tema_lower or "educativo" in tema_lower:
        hashtags.extend([
            "#ComunidadEducativa",
            "#Estudiantes",
        ])

    if "matrícula" in tema_lower or "matriculas" in tema_lower:
        hashtags.extend([
            "#Matrículas",
            "#EducaciónParaTodos",
        ])

    if objetivo == "INVITACION":
        hashtags.append("#Invitación")

    if objetivo == "RECONOCIMIENTO":
        hashtags.append("#Gratitud")

    hashtags_texto = " ".join(hashtags[:8])

    # Idea visual
    idea_visual = (
        f"Utilizar una fotografía relacionada con {tema_limpio}, "
        f"preferiblemente una imagen real de la actividad. "
        f"Incorporar los colores institucionales verde, naranja y blanco, "
        f"el logo de la Fundación y un título corto que permita identificar rápidamente el tema."
    )

    # Recomendación
    recomendaciones = {
        "FACEBOOK": (
            "Utilizar un texto claro y cercano, acompañado de fotografías reales. "
            "Es recomendable incluir información suficiente para que la comunidad comprenda "
            "el propósito de la publicación."
        ),

        "INSTAGRAM": (
            "Utilizar una imagen llamativa, un texto más corto y una selección de hashtags. "
            "Se recomienda destacar visualmente el mensaje principal."
        ),

        "GENERAL": (
            "Mantener un mensaje sencillo, institucional y fácil de comprender. "
            "Antes de publicar, revisar fechas, nombres y cualquier dato específico."
        ),
    }

    recomendacion = recomendaciones.get(
        red_social,
        recomendaciones["GENERAL"]
    )

    resultado = f"""
TEXTO SUGERIDO

{texto}


HASHTAGS

{hashtags_texto}


IDEA VISUAL

{idea_visual}


RECOMENDACIÓN

{recomendacion}
"""

    return resultado.strip()


@login_required
def asistente_contenido(request):

    resultado = None

    if request.method == "POST":

        form = AsistenteContenidoForm(request.POST)

        if form.is_valid():

            tema = form.cleaned_data["tema"]
            red_social = form.cleaned_data["red_social"]
            objetivo = form.cleaned_data["objetivo"]
            descripcion = form.cleaned_data["descripcion"]

            resultado = generar_contenido_local(
                tema,
                red_social,
                objetivo,
                descripcion,
            )

    else:
        form = AsistenteContenidoForm()

    return render(
        request,
        "asistente_ia/asistente.html",
        {
            "form": form,
            "resultado": resultado,
        },
    )