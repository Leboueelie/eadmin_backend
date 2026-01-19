from django.urls import path
from .views import ListeServiceAdministratifsView

urlpatterns = [
    path('', ListeServiceAdministratifsView.as_view(), name='liste-services'),
]
