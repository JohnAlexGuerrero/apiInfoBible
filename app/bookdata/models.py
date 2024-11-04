from django.db import models
# from django.utils.text import slugify

from django.db.models import Sum, Count

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
    
    def count_chapters(self):
        chapters = [x['chapter'] for x in Reference.objects.filter(book__id=self.id).values('chapter')]
        return len(set(chapters))
    
    def count_verses(self):
        return Reference.objects.filter(book__id=self.id).count()
    

# create Reference model (id, book, chapter, verse, text)
class Reference(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    chapter = models.IntegerField()
    verse = models.IntegerField()
    text = models.TextField()
    

    class Meta:
        verbose_name = ("Reference")
        verbose_name_plural = ("References")

    def __str__(self):
        return f'{self.book.short_name.capitalize()}. {self.chapter}. {self.verse}'

    def ref(self):
        return self.__str__()