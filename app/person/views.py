from django.shortcuts import render
from django.db.models import Q

from person.models import Character, Feature, Genealogy
from person.serializers import CharacterSerializer, FeatureSerializer, GenealogySerializer

from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class CharacterListCreateApiView(generics.ListCreateAPIView):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
    
class CharacterDetailView(APIView):
    def get(self, *args, **kwargs):
        queryset = Feature.objects.filter(character__id=kwargs['pk'])
        serializer = FeatureSerializer(queryset, many=True)
        return Response(serializer.data)

class GenealogyDetailView(APIView):
    def get_character(self, id):
        return Character.objects.get(id=id).id
    
    def get(self, *args, **kwargs):
        queryset = Genealogy.objects.filter(
            Q(character_1__id=self.get_character(self.kwargs['pk']))  | Q(character_2__id=self.get_character(self.kwargs['pk']))
        )
        serializer = GenealogySerializer(queryset, many=True)
        return Response(serializer.data)