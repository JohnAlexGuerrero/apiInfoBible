
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('Home.urls')),
    path('admin/', admin.site.urls),
    path('api/v1/', include('bookdata.urls')),
    path('api/v1/', include('person.urls')),
    path('api/v1/', include('event.urls')),
]
