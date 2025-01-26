from django.db import models
# from django.utils.text import slugify
from rest_framework import response

from django.db.models import Sum, Count

from geography.models import Place


# Create your models here.
# create Book model (id, name book, short name book, category(antiguo o nuevo testamento), descripcion del libro)
class Book(models.Model):
    class Category(models.TextChoices):
        ANTIGUO_TESTAMENTO = 'Antiguo Testamento'
        NUEVO_TESTAMENTO = 'Nuevo Testamento'
        
    name = models.CharField(max_length=50, unique=True)
    short_name = models.CharField(max_length=30, unique=True)
    category = models.CharField(max_length=50, choices=Category.choices)
    description = models.TextField()
    slug = models.SlugField()

    class Meta:
        verbose_name = ("Book")
        verbose_name_plural = ("Books")

    def __str__(self):
        return self.name.upper()
    
    def get_queryset(self):
        return Reference.objects.filter(book__id=self.id)
    
    def count_chapters(self):
        chapters = [x['chapter'] for x in self.get_queryset().values('chapter')]
        return len(set(chapters))
    
    def count_verses(self):
        return self.get_queryset().count()
    
    def get_absolute_url(self):
        return f'http://localhost:8000/api/v1/book/{self.id}/'
    
    def chapters(self):
        list_chapters = [x['chapter'] for x in self.get_queryset().values('chapter')]
        list_chapters_ordering = sorted(list_chapters)
        return [f'http://localhost:8000/api/v1/book/{self.id}/chapter/{y}/' for y in set(list_chapters_ordering)]
    
    def get_events(self):
        references = list(map(lambda x: x.events.all(), self.references.all()))
        
        list_title = []
        list_events = []
        
        for x in references:
            for y in x:
                if y.title not in list_title:
                    list_title.append(y.title)
                    list_events.append(
                        {"title": y.title,"event_url":f'http://localhost:8000/api/v1/event/{y.id}/'}
                    )
                else:
                    continue
            
        return list_events

    def get_characters(self):
        verses = list(map(lambda x : x.events.all(), self.references.all()))
        
        list_characters = []
        list_names = []
        
        for x in verses:
            for y in x:
                for n in y.characters.all():
                    if n.name not in list_names:
                        list_names.append(n.name)
                        list_characters.append(
                            {"name_character": n.name, "character_url": f'http://localhost:8000/api/v1/character/{n.id}/'}
                        )
                    else:
                        continue
        return list_characters

# create Reference model (id, book, chapter, verse, text)
class Reference(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='references')
    chapter = models.IntegerField()
    verse = models.IntegerField()
    text = models.TextField() 

    class Meta:
        ordering = ('chapter','verse')
        verbose_name = ("Reference")
        verbose_name_plural = ("References")

    def __str__(self):
        return f'{self.book.short_name.capitalize()}. {self.chapter}. {self.verse}'

    def ref(self):
        return self.__str__()
    
    def get_absolute_url(self):
        return f'http://localhost:8000/api/v1/verse/{self.id}/'
    
    def get_links(self):
        links = []
        
        if self.refs.all():
            for x in self.refs.all():
                for y in x.links_references.all():
                    links.append({"link_name": f'{y}',"link_url":f'http://localhost:8000/api/v1/verse/{y.id}'})            
        return links

# modelo Links, este metodo permite la relacion entre versiculos, con cardinalidad n:m
class Link(models.Model):
    reference = models.ForeignKey(Reference, on_delete=models.CASCADE, related_name="refs")
    links_references = models.ManyToManyField(Reference, verbose_name=("link"), related_name="links")

    class Meta:
        verbose_name = ("Link")
        verbose_name_plural = ("Links")

    def __str__(self):
        return f"{self.reference.ref}"



#model relaciona la Place table with the Reference table
class PlaceReference(models.Model):
    verse = models.ForeignKey(Reference, on_delete=models.CASCADE)
    place = models.ForeignKey(Place, on_delete=models.CASCADE)

    class Meta:
        verbose_name = ("PlaceReference")
        verbose_name_plural = ("PlaceReferences")

    def __str__(self):
        return self.place.__str__
