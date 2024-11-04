from django.shortcuts import render

from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics

from bookdata.serializers import BookSerializer, ReferenceSerializer
from bookdata.models import Book, Reference

# Create your views here.
class BookListCreateApiView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class ReferenceListCreateApiView(generics.ListCreateAPIView):
    queryset = Reference.objects.all()
    serializer_class = ReferenceSerializer
    
class ReferenceDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reference.objects.all()
    serializer_class = ReferenceSerializer