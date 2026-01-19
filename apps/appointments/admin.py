from django.contrib import admin
from .models import RendezVous

# Register your models here.
@admin.register(RendezVous)
class RendezVousAdmin(admin.ModelAdmin):
    list_display = ('utilisateur', 'creneau', 'statut', 'date_creation',)
    list_filter = ('statut',)
    search_fields = ('utilisateur__username',)
    ordering = ('-date_creation',)