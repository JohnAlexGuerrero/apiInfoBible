from django.contrib import admin

from bookdata.models import Book, Reference


# Register your models here.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['name', 'short_name']

@admin.register(Reference)
class ReferenceAdmin(admin.ModelAdmin):
    list_display = ['__str__','text']
    ordering = ('id',)