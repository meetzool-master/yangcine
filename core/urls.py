from django.urls import path
from movies import views as movie_views

app_name = "core"

urlpatterns = [
    path("", movie_views.HomeView.as_view(), name="home"),
    path("cine", movie_views.CineView.as_view(), name="cine"),
    path("corner", movie_views.CornerView.as_view(), name="corner"),
    path("yangcine", movie_views.YangcineView.as_view(), name="yangcine"),
]