from rest_framework import serializers

from person.models import Character, Feature, Genealogy

from bookdata.serializers import ReferenceSerializer


class CharacterSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Character
        fields = [
            'name',
            'get_absolute_url',
            'get_genealogy_url',
            'count_characters',
            'histories',
        ]
        
class FeatureSerializer(serializers.ModelSerializer):    
    verse = ReferenceSerializer()
    
    class Meta:
        model = Feature
        fields = [
            'name',
            'verse',
        ]

class GenealogySerializer(serializers.ModelSerializer):
    character_1 = CharacterSerializer()
    character_2 = CharacterSerializer()
    verse = ReferenceSerializer()
    
    class Meta:
        model = Genealogy
        fields = [
            'character_1',
            'character_2',
            'type',
            'verse',
        ]