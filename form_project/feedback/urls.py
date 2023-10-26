from django.urls import path
from . import views

urlpatterns = [
    path('done', views.DoneView.as_view()),
    path('', views.FeedBackView.as_view()),
    path('update/<int:pk>', views.FeedBackViewUpdate.as_view()),
    path('list', views.ListFeedBack.as_view()),
    path('detail/<int:pk>', views.DetailFeedBack.as_view()),
]
