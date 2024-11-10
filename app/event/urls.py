from django.urls import path

from event.views import EventListCreateApiView

urlpatterns = [
    path('events/', EventListCreateApiView.as_view(), name='events'),
]
