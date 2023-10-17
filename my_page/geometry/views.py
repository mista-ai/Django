from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseNotFound
from django.shortcuts import redirect
from django.urls import reverse


# Create your views here.

def get_rectangle_area(request, width, height):
    return HttpResponse(f"Площадь прямоугольника размером {width}x{height} равна {width * height}")


def get_square_area(request, width):
    return HttpResponse(f"Площадь квадрата размером {width}x{width} равна {width * width}")


def get_circle_area(request, radius):
    return HttpResponse(f"Площадь круга радиусом {radius} равна {3.14 * radius * radius}")


def get_rectangle_area_redirect(request, width, height):
    redirect_url = reverse('rectangle', args=(width, height))
    return redirect(f"{redirect_url}")


def get_square_area_redirect(request, width):
    redirect_url = reverse('square', args=(width,))
    return redirect(f"{redirect_url}")


def get_circle_area_redirect(request, radius):
    redirect_url = reverse('circle', args=(radius,))
    return redirect(f"{redirect_url}")


def get_figure(request, figure):
    return render(request, f'geometry/{figure}.html')
