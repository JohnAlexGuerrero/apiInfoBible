from django.urls import path

from event.views import EventListCreateApiView, EventRetrieveUpdateApiView

urlpatterns = [
    path('events/', EventListCreateApiView.as_view(), name='events'),
    path('event/<int:pk>/', EventRetrieveUpdateApiView.as_view(), name='detail_event'),
]
