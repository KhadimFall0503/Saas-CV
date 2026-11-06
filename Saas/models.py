from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class CV(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="cvs")

    # Infos personnelles
    nom = models.CharField(max_length=120)
    email = models.EmailField()
    telephone = models.CharField(max_length=30)
    adresse = models.CharField(max_length=255, blank=True, null=True)

    # Contenu CV structuré
    profil = models.TextField(help_text="Résumé professionnel")
    competences = models.TextField(help_text="Compétences séparées par virgule")

    experience = models.TextField(help_text="Expériences professionnelles")
    formation = models.TextField(help_text="Études / diplômes")

    langues = models.CharField(max_length=255, blank=True, null=True)
    interets = models.CharField(max_length=255, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.nom
class Meta:
    verbose_name = "CV"
    verbose_name_plural = "CVs"
    
    
from django.db import models

class TemplateCV(models.Model):
    CATEGORY_CHOICES = [
        ('tech', 'Technologie'),
        ('finance', 'Finance'),
        ('design', 'Design'),
        ('sante', 'Santé'),
        ('education', 'Éducation'),
        ('business', 'Business'),
        ('classic', 'Classique'),
    ]

    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)

    description = models.TextField()

    # style visuel
    color_class = models.CharField(max_length=50)

    # structure du CV (IMPORTANT)
    has_photo = models.BooleanField(default=True)
    has_skills = models.BooleanField(default=True)
    has_experience = models.BooleanField(default=True)
    has_education = models.BooleanField(default=True)
    has_languages = models.BooleanField(default=False)
    has_interests = models.BooleanField(default=False)

    # design flags
    is_popular = models.BooleanField(default=False)
    is_new = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.name
