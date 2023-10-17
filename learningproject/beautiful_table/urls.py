from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_beautiful_table_index, name='beautiful_table-index')
]