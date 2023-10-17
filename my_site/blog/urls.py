from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page),
    path('people', views.get_people)
]