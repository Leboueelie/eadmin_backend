from django.db import models
from django.contrib.auth.models import User
from apps.scheduling.models import CreneauHoraire

# Create your models here.
class RendezVous(models.Model):
    """
    Représente un rendez-vous pris par l'utilisateur
    """

    STATUT_RESERVE = "reserve"
    STATUT_ANNULE = "annule"

    CHOIX_STATUT = [
        (STATUT_RESERVE, 'Réservé'),
        (STATUT_ANNULE, 'Annulé'),
    ]
    utilisateur = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='rendez_vous',
        help_text="Utilisateur ayant réservé le rendez-vous"
    )
    creneau = models.OneToOneField(
        CreneauHoraire, 
        on_delete=models.CASCADE, 
        related_name='rendez_vous',
        help_text='Créneau Horaire réservé',
    )
    statut = models.CharField(
        max_length=10,
        choices=CHOIX_STATUT,
        default=STATUT_RESERVE,
        help_text="Statut du rendez-vous",
    )
    date_creation = models.DateTimeField(
        auto_now_add=True, 
        help_text="Date e création du rendez vous"
    )

    class Meta:
        verbose_name = 'Rendez-vous'
        verbose_name_plural = 'Rendez-vous'
        ordering = ['-date_creation']
    
    def __str__(self):
        return f"{self.utilisateur.username} - {self.creneau}"
    