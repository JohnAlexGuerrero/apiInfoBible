from django.urls import path

from bookdata.models import Book, Reference

from bookdata.views import BookListCreateApiView, ReferenceListCreateApiView, ReferenceDetailView

urlpatterns = [
    path('books/', BookListCreateApiView.as_view(), name='books'),
    path('verses/', ReferenceListCreateApiView.as_view(), name='list_verses'),
    path('verses/<int:pk>/', ReferenceDetailView.as_view(), name='detail_verse'),
]

