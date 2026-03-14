from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class CV(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nom = models.CharField(max_length=100)
    email = models.EmailField()
    telephone = models.CharField(max_length=20)
    profil = models.TextField()
    experience = models.TextField()
    education = models.TextField()
    competences = models.TextField()

    def __str__(self):
        return self.nom
class Meta:
    verbose_name = "CV"
    verbose_name_plural = "CVs"
