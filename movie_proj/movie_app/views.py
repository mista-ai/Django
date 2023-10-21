from django.shortcuts import render, get_object_or_404
from django.db.models import F, Value
# Create your views here.
from .models import Movie


def show_all_movies(request):
    # movies = Movie.objects.order_by(F('year').asc(nulls_last=True), '-rating')
    movies = Movie.objects.annotate(
        true_bool=Value(True),
        false_bool=Value(False),
        str_field=Value('hello'),
        int_field=Value(123),
        new_budget=F('budget')+100,
        rating_year=F('rating')*F('year'),
    ).annotate(ffff=F('rating')*F('budget'))
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
