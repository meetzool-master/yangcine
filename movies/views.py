from datetime import date
from django.shortcuts import render
from django.views.generic import ListView
from . import models

# Create your views here.
"""
urlpatterns = [
    path("", movie_views.HomeView.as_view(), name="home"),
    path("cine", movie_views.CineView.as_view(), name="cine"),
    path("corner", movie_views.CornerView.as_view(), name="corner"),
    path("yangcine", movie_views.YangcineView.as_view(), name="yangcine"),
    path("random", movie_views.RandomView.as_view(), name="random"),
]
"""


class HomeView(ListView):
    model = models.Movie
    paginate_by = 6
    paginate_orphans = 1
    ordering = "-created"
    def get_queryset(self):
        queryset = models.Movie.objects.order_by('?')
        return queryset


class CineView(ListView):
    model = models.Movie
    paginate_by = 6
    paginate_orphans = 1
    def get_queryset(self):
        queryset = models.Movie.objects.filter(source__pk=1).order_by('-created')
        return queryset

class CornerView(ListView):
    model = models.Movie
    paginate_by = 6
    paginate_orphans = 1
    def get_queryset(self):
        queryset = models.Movie.objects.filter(source__pk=2).order_by('-created')
        return queryset
    
class YangcineView(ListView):
    model = models.Movie
    paginate_by = 6
    paginate_orphans = 1
    def get_queryset(self):
        queryset = models.Movie.objects.filter(source__pk=3).order_by('-created')
        return queryset
    
    


def movie_detail(request, pk):
    movie = models.Movie.objects.get(pk=pk)
    return render(request, "movies/detail.html", {"movie" : movie})
