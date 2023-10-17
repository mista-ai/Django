from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseNotFound


# Create your views here.
def get_post_by_name(request, name_post):
    data = {
        'name_post': name_post.title(),
    }
    return render(request, 'blog/detail_by_name.html', data)


def get_post_by_number(request, number_post):
    data = {
        'number_post': number_post,
    }
    return render(request, 'blog/detail_by_number.html', data)


def get_posts(request):
    return render(request, 'blog/list_detail.html')


def get_kianu(request):
    data = {
        'year_born': 1964,
        'city_born': 'Бейрут',
        'movie_name': 'На гребне волны',
    }
    return render(request, 'posts/kianu.html', data)


def get_guinness_world_records(request):
    context = {
        'power_man': 'Narve Laeret',
        'bar_name': 'Bob’s BBQ & Grill',
        'count_needle': 1790,
    }
    return render(request, 'posts/guinnessworldrecords.html', context=context)
