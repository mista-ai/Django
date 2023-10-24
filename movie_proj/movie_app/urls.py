from . import views
from django.urls import path

urlpatterns = [
    path('', views.show_all_movies),
    path('movie/<slug:slug_movie>', views.show_one_movie, name='movie-detail'),
    path('directors', views.show_all_dirctors),
    path('director/<slug:slug_director>', views.show_one_director, name='director-detail'),
    # path('directors/<slug:slug_director', views.show_one_movie, name='director-detail')
]
