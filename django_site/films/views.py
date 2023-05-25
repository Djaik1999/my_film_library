from django.shortcuts import render
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView
from django.urls import reverse_lazy, reverse

from .models import Movie, CastMember


class MovieListView(ListView):
    model = Movie
    template_name = "movies/movie_list_view.html"
    context_object_name = "movies"


class MovieDetailView(DetailView):
    model = Movie
    template_name = "movies/movie_detail_view.html"
    context_object_name = "movie"
    slug_url_kwarg = "slug"


class CastListView(ListView):
    model = CastMember
    template_name = "movies/cast_list_view.html"
    context_object_name = "cast_members"
