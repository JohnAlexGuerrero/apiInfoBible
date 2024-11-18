from django.contrib import admin

from bookdata.models import Book, Reference, PlaceReference
from person.models import Character, Feature, Genealogy
from geography.models import Place
from event.models import Event

# Register your models here.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['name', 'short_name']

@admin.register(Reference)
class ReferenceAdmin(admin.ModelAdmin):
    list_display = ['__str__','text']
    ordering = ('book',)

@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    pass

@admin.register(PlaceReference)
class PlaceReferenceAdmin(admin.ModelAdmin):
    pass


@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    pass

@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    pass

@admin.register(Genealogy)
class GenealogyAdmin(admin.ModelAdmin):
    pass

# event
@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    pass
