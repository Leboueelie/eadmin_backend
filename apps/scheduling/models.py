from django.db import models
from apps.services.models import ServiceAdministratif

# Create your models here.
class CreneauHoraire(models.Model):
    """
    Représente un creneau horaire disponible pour un service administratif
    """

    service = models.ForeignKey(ServiceAdministratif, on_delete=models.CASCADE, related_name='creneaux', help_text="Service admin concerné par le creneau")
    date = models.DateField(help_text="date du creneau")
    heure_debut = models.TimeField(help_text="Heure de début du creneau")
    heure_fin = models.TimeField(help_text="Heure de fin du creneau")
    disponible = models.BooleanField(default=True, help_text="Indique si le créneau est disponible à la réservation")
    date_creation = models.DateTimeField(auto_now_add=True, help_text="Date de création du créneau")

    class Meta:
        verbose_name = "Créneau horaie"
        verbose_name_plural = "Créneaux horaires"
        ordering = ['date', 'heure_debut']
        unique_together = (
            'service',
            'date',
            'heure_debut',
            'heure_fin',
        )
    
    def __str__(self):
        """
        Représentation lisible du créneau
        """
        return f"{self.service.nom} - {self.date} ({self.heure_debut} {self.heure_fin})"