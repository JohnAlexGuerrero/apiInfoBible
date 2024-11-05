from django.db import models

# Create your models here.
class Place(models.Model):
    class Category(models.TextChoices):
        RIO = 'rio'
        REGION_GEOGRAFICA = 'Región Geografica'
        
    name = models.CharField(max_length=50, unique=True)
    latitude = models.CharField(max_length=30, null=True, blank=True)
    longitude = models.CharField(max_length=30, null=True, blank=True)
    category = models.CharField(max_length=50, choices=Category.choices)

    class Meta:
        verbose_name = ("Place")
        verbose_name_plural = ("Places")

    def __str__(self):
        return self.name
