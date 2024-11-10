from rest_framework import serializers

from event.models import Event

from bookdata.serializers import ReferenceSerializer
from person.serializers import CharacterSerializer

class EventSerializer(serializers.ModelSerializer):
    characters = CharacterSerializer(many=True)
    verses = ReferenceSerializer(many=True)
    
    class Meta:
        model = Event
        fields = [
            'title',
            'characters',
            'verses'
        ]