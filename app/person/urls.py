from django.urls import path

from person.views import CharacterListCreateApiView, CharacterDetailView
from person.views import GenealogyDetailView

urlpatterns = [
    path('characters/', CharacterListCreateApiView.as_view(), name='list_characters'),
    path('character/<int:pk>/', CharacterDetailView.as_view(), name='detail_character'),
    path('character/<int:pk>/genealogy/', GenealogyDetailView.as_view(), name='genealogy_character'),
]
