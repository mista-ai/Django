from django.shortcuts import render, get_object_or_404
from django.db.models import F, Value
# Create your views here.
from .models import Movie, Director


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

def show_all_dirctors(request):
    directors = Director.objects.all()
    for director in directors:
        if director.slug == '':
            director.save()
    return render(request, 'movie_app/all_directors.html', {'directors': directors})

def show_one_director(request, slug_director):
    pass