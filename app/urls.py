from django.contrib import admin
from django.urls import path
from genres.views import GenreCreateListVieww, GenreRetrieveUpdateDestroyView
from actors.views import ActorCreateListView, ActorRetriveUpdateDestroyView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('genres/', GenreCreateListVieww.as_view(), name='genre-create-list'),
    path('genres/<int:pk>/', GenreRetrieveUpdateDestroyView.as_view(), name='genre-detail-view'),
    path('actors/', ActorCreateListView.as_view(), name='actor-create-list'),
    path('actors/<int:pk>/', ActorRetriveUpdateDestroyView.as_view(), name='actor-detail-list')
    
    
]
