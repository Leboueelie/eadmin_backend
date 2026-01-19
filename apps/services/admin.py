from django.contrib import admin
from .models import ServiceAdministratif

# Register your models here.
@admin.register(ServiceAdministratif)
class ServiceAdministratifAdmin(admin.ModelAdmin):
    """
    configuration d'affichage du modèle ServiceAdministratif dans l'admin Django
    """
    list_display = ('nom', 'actif', 'date_creation')
    list_filter = ('actif',)
    search_fields = ('nom',)
    ordering = ('nom',)