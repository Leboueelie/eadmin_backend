from rest_framework import generics
from .models import CreneauHoraire
from .serializers import CreneauHoraireSerializer

# Create your views here.
class ListeCreneauxDisponibleView(generics.ListAPIView):
    """
    Retourne les creneaux disponible
    possibilité de filtrer par service
    """

    serializer_class = CreneauHoraireSerializer

    def get_queryset(self):
        """
        filtrage optionnel par service administratif
        """
        queryset = CreneauHoraire.objects.filter(disponible=True)
        service_id = self.request.query_params.get('service')
        queryset = queryset.filter(service_id=service_id)

        return queryset