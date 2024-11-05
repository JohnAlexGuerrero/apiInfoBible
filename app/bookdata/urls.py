from django.urls import path


from bookdata.views import BookListCreateApiView, BookDetailView
from bookdata.views import ReferenceListCreateApiView, ReferenceDetailView, ChapterDetail

urlpatterns = [
    path('books/', BookListCreateApiView.as_view(), name='books'),
    path('book/<int:pk>/', BookDetailView.as_view(), name='detail_book'),
    path('book/<int:pk>/chapter/<int:num_chapter>/', ChapterDetail.as_view(), name='detail_chapter'),

    path('verses/', ReferenceListCreateApiView.as_view(), name='list_verses'),
    path('verse/<int:pk>/', ReferenceDetailView.as_view(), name='detail_verse'),
]
