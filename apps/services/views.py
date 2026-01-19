from rest_framework import generics
from .models import ServiceAdministratif
from .serializers import ServiceAdministratifSerializer

# Create your views here.
class ListeServiceAdministratifsView(generics.ListAPIView):
    """
    Retourne la liste des services administratifs actifs
    accès public
    """
    queryset = ServiceAdministratif.objects.filter(actif=True)
    serializer_class = ServiceAdministratifSerializer