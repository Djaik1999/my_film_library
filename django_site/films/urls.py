from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import MovieListView, MovieDetailView


urlpatterns = [
    path('', MovieListView.as_view(), name="movie-list-view"),
    path("movie/<slug:slug>", MovieDetailView.as_view(), name="movie-detail"),
    
]
