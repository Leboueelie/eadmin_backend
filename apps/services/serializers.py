from rest_framework import serializers
from .models import ServiceAdministratif

class ServiceAdministratifSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceAdministratif
        fields = [
            'id',
            'nom',
            'description',
            'actif',
            'date_creation',
        ]
        read_only_fields = ['id', 'date_creation']