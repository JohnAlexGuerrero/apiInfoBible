from rest_framework import serializers

from bookdata.models import Book, Reference

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = [
            'name',
            'slug',
            'short_name',
            'category',
            'description',
            'count_chapters',
            'count_verses',
            'get_absolute_url',
            'chapters',
            'get_events',
            'get_characters',
        ]
        
class ReferenceSerializer(serializers.ModelSerializer):       
    class Meta:
        model = Reference
        fields = [
            'ref',
            'text',
            'get_absolute_url',
            'get_links',
        ]
        