from rest_framework import generics, status, permissions
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import RendezVous
from .serializers import RendezVousSerializer, AnnulationRendezVousSerializer
from apps.scheduling.models import CreneauHoraire


# Create your views here.
class CreerRendezVousView(generics.CreateAPIView):
    """
    permet à l'utilisateur authentifié de créer un rendez vous
    """
    serializer_class = RendezVousSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        """
        création de rendez vous avec validation métier
        """
        creneau_id = request.data.get('creneau')
        creneau = get_object_or_404(CreneauHoraire, id=creneau_id, disponible=True)
        rendez_vous = RendezVous.objects.create(utilisateur=request.user, creneau=creneau)

        # Le creneau devient indisponible
        creneau.disponible = False
        creneau.save()
        serializer = self.get_serializer(rendez_vous)

        return Response(serializer.data, status=status.HTTP_201_CREATED)
    

class AnnulerRendezVousView(generics.DestroyAPIView):
    """
   Permet à l'utilisateur d'annuler son rendez vous
    """
    serializer_class = AnnulationRendezVousSerializer

    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        """
        annulation du rendez vous et liberation du creneau
        """
        rendez_vous = get_object_or_404(RendezVous, id=kwargs['pk'], utilisateur=request.user)
        creneau = rendez_vous.creneau
        creneau.disponible = True
        creneau.save()

        rendez_vous.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)