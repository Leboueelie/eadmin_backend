from rest_framework import serializers
from .models import CreneauHoraire

class CreneauHoraireSerializer(serializers.ModelSerializer):
    service_nom = serializers.CharField(source='service.nom', read_only=True)

    class Meta:
        model = CreneauHoraire
        fields = [
            'id',
            'service',
            'service_nom',
            'date',
            'heure_debut',
            'heure_fin',
            'disponible',
        ]
        read_only_fields = ['id']