"""
Routes de l'APi - Version 1
toutes les applications exposent leurs endpoint ici
"""

from django.urls import path, include
from drf_spectacular.views import (SpectacularAPIView, SpectacularSwaggerView,)

urlpatterns = [
    # Shéma OpenAPI (JSON)
    path('shema/', SpectacularAPIView.as_view(), name='shema'),

    # Interface Swagger
    path('docs/', SpectacularSwaggerView.as_view(url_name='shema'), name='swagger-iu'),

    path('auth/', include('authentication.urls')),
    path('services/', include('apps.services.urls')),
    path('creneaux/', include('apps.scheduling.urls')),
    path('rendez-vous/', include('apps.appointments.urls')),
]