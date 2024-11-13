from django.db import models

from bookdata.models import Reference
from person.models import Character

# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=50, unique=True)
    characters = models.ManyToManyField(Character, verbose_name=("characters"), related_name='characters', blank=True)
    verses = models.ManyToManyField(Reference, verbose_name=("verses"), related_name='events')

    class Meta:
        verbose_name = ("Event")
        verbose_name_plural = ("Events")

    def __str__(self):
        return self.title.upper()

    def get_absolute_url(self):
        return f'http://localhost:8000/api/v1/event/{self.id}/'
    
    def get_title(self):
        return self.title