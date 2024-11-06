from django.db import models

# Create your models here.
class Character(models.Model):
    class Classification(models.TextChoices):
        VARON = 'Varón'
        VARONA = 'Varona'
        
    name = models.CharField(max_length=150, unique=True)
    feature = models.CharField(max_length=150, blank=True, null=True)
    classification = models.CharField(max_length=50, choices=Classification.choices)

    class Meta:
        verbose_name = ("Character")
        verbose_name_plural = ("Characters")

    def __str__(self):
        return self.name.capitalize()
