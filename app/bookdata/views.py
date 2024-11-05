from django.shortcuts import render
from django.db.models import Q

from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework.views import APIView

from bookdata.serializers import BookSerializer, ReferenceSerializer
from bookdata.models import Book, Reference

# Create your views here.
class BookListCreateApiView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class ChapterDetail(APIView):
    def get(self, *args, **kwargs):
        queryset = Reference.objects.filter(book__id=kwargs['pk']).filter(chapter=kwargs['num_chapter'])
        serializer = ReferenceSerializer(queryset, many=True)
        return Response(serializer.data)
    

class ReferenceListCreateApiView(generics.ListCreateAPIView):
    queryset = Reference.objects.all()
    serializer_class = ReferenceSerializer
    
class ReferenceDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reference.objects.all()
    serializer_class = ReferenceSerializer