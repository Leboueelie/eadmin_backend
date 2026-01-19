from django.urls import path
from .views import ListeCreneauxDisponibleView

urlpatterns = [
    path('disponibles/', ListeCreneauxDisponibleView.as_view(), name='creneaux-disponible')
]
