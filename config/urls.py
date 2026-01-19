"""
Gestion des routes principales de l'API
Tout les routes sont versionnées
"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Interface d'administration Django
    path('admin/', admin.site.urls),

    # Routes de l'API version 1
    path('', include('config.api_urls_v1')),

]
