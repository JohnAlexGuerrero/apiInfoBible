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
        ]
        
class ReferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reference
        fields = [
            'ref',
            'text'
        ]