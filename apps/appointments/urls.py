from django.urls import path
from .views import CreerRendezVousView, AnnulerRendezVousView

urlpatterns = [
    path('', CreerRendezVousView.as_view(), name='creer-rendez-vous'),
    path('<int:pk>/', AnnulerRendezVousView.as_view(), name='annuler-rendez-vous'),
]
