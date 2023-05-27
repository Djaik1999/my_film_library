from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import MovieListView, MovieDetailView, CastListView, CastDetailView


urlpatterns = [
    path('', MovieListView.as_view(), name="movies-list"),
    path("movie/<slug:slug>", MovieDetailView.as_view(), name="movie-detail"),
    path("cast-members/", CastListView.as_view(), name="cast-members-list"),
    path("cast-member/<slug:slug>", CastDetailView.as_view(), name="cast-member-detail"),
]
