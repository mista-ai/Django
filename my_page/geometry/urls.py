from django.urls import path
from . import views

urlpatterns = [

    path('rectangle/<int:width>/<int:height>', views.get_rectangle_area, name='rectangle'),
    path('square/<int:width>', views.get_square_area, name='square'),
    path('circle/<int:radius>', views.get_circle_area, name='circle'),
    path('get_rectangle_area/<int:width>/<int:height>', views.get_rectangle_area_redirect),
    path('get_square_area/<int:width>', views.get_square_area_redirect),
    path('get_circle_area/<int:radius>', views.get_circle_area_redirect),
    path('<str:figure>', views.get_figure)
]
