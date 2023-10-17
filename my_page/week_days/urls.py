from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_index),
    path('<int:weekday>/', views.get_weekday_by_number),
    path('<str:weekday>/', views.get_weekday_by_str, name='todo-name'),
]