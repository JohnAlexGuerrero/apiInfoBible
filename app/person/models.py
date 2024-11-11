from django.db import models

from bookdata.models import Reference

# Create your models here.
class Character(models.Model):    
    name = models.CharField(max_length=150, unique=True)
    tribe = models.CharField(max_length=50, blank=True, null=True)
    
    class Meta:
        verbose_name = ("Character")
        verbose_name_plural = ("Characters")

    def __str__(self):
        return self.name.capitalize()
    
    def get_absolute_url(self):
        return f'http://localhost:8000/api/v1/character/{self.id}/'
    
    def get_genealogy_url(self):
        return f'http://localhost:8000/api/v1/character/{self.id}/genealogy/'
    
    def count_characters(self):
        return Genealogy.objects.filter(character_1__id=self.id).count()
    
    def histories(self):
        list_events = []
        events = self.characters.all()
        for x in events:
            list_events.append({"title":x.title,"url":f'http://localhost:8000/api/v1/event/{x.id}/'})
        return list_events
    

class Feature(models.Model):
    name = models.CharField(max_length=150, blank=True, null=True)
    verse = models.ForeignKey(Reference, on_delete=models.CASCADE)
    character = models.ForeignKey(Character, on_delete=models.CASCADE, related_name='feature')
    
    class Meta:
        verbose_name = ("Feature")
        verbose_name_plural = ("Features")

    def __str__(self):
        return f'{self.name.capitalize()} -> {self.character.__str__()}'


class Genealogy(models.Model):
    class Type(models.TextChoices):
        PADRE = 'padre'
        MADRE = 'madre'
        HIJO = 'hijo(a)'
        ESPOSA = 'esposo(a)'
        
    character_1 = models.ForeignKey(Character, on_delete=models.CASCADE, related_name='character_1')
    character_2 = models.ForeignKey(Character, on_delete=models.CASCADE, related_name='character_2')
    type = models.CharField(max_length=50, choices=Type.choices)
    verse = models.ForeignKey(Reference, on_delete=models.CASCADE)


    class Meta:
        unique_together = ('character_1','character_2')
        verbose_name = ("Genealogy")
        verbose_name_plural = ("Genealogies")

    def __str__(self):
        return f'{self.character_1.name} - {self.type} - {self.character_2.name}'

    def get_absolute_url(self):
        return f'http://localhost:8000/api/v1/character/{self.id}/genealogy/'
