from django.contrib import admin

from bookdata.models import Book, Reference, PersonReference, PlaceReference
from person.models import Character
from geography.models import Place


# Register your models here.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['name', 'short_name']

@admin.register(Reference)
class ReferenceAdmin(admin.ModelAdmin):
    list_display = ['__str__','text']
    ordering = ('id',)

@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    pass

@admin.register(PlaceReference)
class PlaceReferenceAdmin(admin.ModelAdmin):
    pass


@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    pass

@admin.register(PersonReference)
class PersonReferenceAdmin(admin.ModelAdmin):
    pass
