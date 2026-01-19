from django.db import models

# Create your models here.
class ServiceAdministratif(models.Model):
    """
    Représente un service administratif (mairie, préfecture, etc..)
    """

    nom = models.CharField(max_length=150, unique=True, help_text="Nom du service administratif")
    description = models.TextField(blank=True, help_text="Description détaillée du service")
    actif = models.BooleanField(default=True, help_text="Indique si le service est actuellement actif")
    date_creation = models.DateTimeField(auto_now_add=True, help_text="date de création du service")

    class Meta:
        verbose_name = "Service administratif"
        verbose_name_plural = "Services administratifs"
        ordering = ['nom']

    def __str__(self):
        """
        Représentation lisible du service dans l'admin Django
        """
        return self.nom