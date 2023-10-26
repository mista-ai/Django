from django.shortcuts import render, get_object_or_404
from django.db.models import F, Value
# Create your views here.
from .models import Movie, Director, Actor
from django.views.generic.list import ListView


class ListDirectors(ListView):
    template_name = 'movie_app/all_directors.html'
    model = Director
    context_object_name = 'directors'

class ListActors(ListView):
    template_name = 'movie_app/all_actors.html'
    model = Actor
    context_object_name = 'actors'

def show_all_movies(request):
    # movies = Movie.objects.order_by(F('year').asc(nulls_last=True), '-rating')
    movies = Movie.objects.all()
    for movie in movies:
        if movie.slug == '':
            movie.save()
    return render(request, 'movie_app/all_movies.html', {
        'movies': movies
    })


def show_one_movie(request, slug_movie: str):
    movie = get_object_or_404(Movie, slug=slug_movie)
    return render(request, 'movie_app/one_movie.html', {
        'movie': movie
    })


# def show_all_dirctors(request):
#     directors = Director.objects.all()
#     # for director in directors:
#     #     if director.slug == '':
#     #         director.save()
#     return render(request, 'movie_app/all_directors.html', {'directors': directors})


def show_one_director(request, slug_director):
    director = get_object_or_404(Director, slug=slug_director)
    return render(request, 'movie_app/one_director.html', {
        'director': director
    })


# def show_all_actors(request):
#     actors = Actor.objects.all()
#     return render(request, 'movie_app/all_actors.html', {'actors': actors})


def show_one_actor(request, slug_actor):
    actor = get_object_or_404(Actor, slug=slug_actor)
    return render(request, 'movie_app/one_actor.html', {'actor': actor})
