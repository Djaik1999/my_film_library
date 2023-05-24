from django.shortcuts import render
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView
from django.urls import reverse_lazy, reverse

from .models import Movie


class MovieListView(ListView):
    model = Movie
    template_name = "movies/list_view.html"
    context_object_name = "movies"


class MovieDetailView(DetailView):
    model = Movie
    template_name = "movies/detail_view.html"
    context_object_name = "movie"
    slug_url_kwarg = "slug"

