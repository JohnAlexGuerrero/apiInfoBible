from django.shortcuts import render

from event.models import Event

from event.serializers import EventSerializer

from rest_framework import generics

# Create your views here.
class EventListCreateApiView(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class EventRetrieveUpdateApiView(generics.RetrieveUpdateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer