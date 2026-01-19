from rest_framework import serializers
from .models import RendezVous

class RendezVousSerializer(serializers.ModelSerializer):
    utilisateur = serializers.StringRelatedField(read_only=True)
    service = serializers.CharField(source='creneau.service.nom', read_only=True)
    date = serializers.DateField(source='creneau.date', read_only=True)
    heure_debut = serializers.TimeField(source='creneau.heure_debut', read_only=True)
    heure_fin = serializers.TimeField(source='creneau.heure_fin', read_only=True)

    class Meta:
        model = RendezVous
        fields = (
            'id',
            'utilisateur',
            'service',
            'date',
            'heure_debut',
            'heure_fin',
            'statut',
            'date_creation'
        )
        read_only_fields = ['id', 'utilisateur', 'date_craetion',]


class AnnulationRendezVousSerializer(serializers.Serializer):
    confirmation = serializers.BooleanField()