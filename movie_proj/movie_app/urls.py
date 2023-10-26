from . import views
from django.urls import path

urlpatterns = [
    path('', views.show_all_movies),
    path('movie/<slug:slug_movie>', views.show_one_movie, name='movie-detail'),
    path('directors', views.ListDirectors.as_view()),
    path('director/<slug:slug_director>', views.show_one_director, name='director-detail'),
    path('actors', views.ListActors.as_view()),
    path('actor/<slug:slug_actor>', views.show_one_actor, name='actor-detail'),
    # path('directors/<slug:slug_director', views.show_one_movie, name='director-detail')
]
