from django.db import models

# Create your models here.
class Person(models.Model):
    class Gender(models.TextChoices):
        VARON = 'Varón'
        VARONA = 'Varona'
        
    name = models.CharField(max_length=150, unique=True)
    sex = models.CharField(max_length=30, choices=Gender.choices)
    feature = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        verbose_name = ("Person")
        verbose_name_plural = ("Persons")

    def __str__(self):
        return self.name.capitalize()
