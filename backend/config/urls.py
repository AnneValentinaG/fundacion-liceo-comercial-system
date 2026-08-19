from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("cuentas/", include("django.contrib.auth.urls")),
    path("documentos/", include("documentos.urls"),),
    path("contratos/", include("contratos.urls"),),
    path("publicaciones/", include("publicaciones.urls"),),
    path("metricas/", include("metricas.urls"),),
    path("asistente-ia/",include("asistente_ia.urls"),),
    path("comunicaciones/", include("comunicaciones.urls"),),
    path("", include("core.urls"),),
    
]


if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )


