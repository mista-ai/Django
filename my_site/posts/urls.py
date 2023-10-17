from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_posts),
    path('kianu', views.get_kianu),
    path('guinness', views.get_guinness_world_records),
    path('<int:number_post>', views.get_post_by_number),
    path('<str:name_post>', views.get_post_by_name),
]
