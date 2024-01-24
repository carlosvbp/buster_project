from django.urls import path
from movies.views import MovieDeatailView, MovieView

urlpatterns = [
    path("movies/", MovieView.as_view()),
    path("movies/<int:movie_id>/", MovieDeatailView.as_view()),
]
