from django.contrib import admin
from .models import CreneauHoraire

# Register your models here.
@admin.register(CreneauHoraire)
class CreneauHoraireAdmin(admin.ModelAdmin):
    """
    Configuration d'affichage du modèle creneauHoraire dans l'admin Django
    """

    list_display = ('service', 'date', 'heure_debut', 'heure_fin', 'disponible')
    list_filter = ('service', 'date', 'disponible')
    ordering = ('date', 'heure_debut')