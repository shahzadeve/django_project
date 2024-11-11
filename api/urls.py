# API app urls  there we use api urls for my app not for my project

from django.urls import path
from .views import *

urlpatterns = [
   
    path('list/', WatchList.as_view(), name='movieslist'), #api/list/
    path('detail/<int:pk>/', WatchDetails.as_view(), name='moviedetail'), #api/detail/<int:pk>/

    
    path('stream/', StreamPlatformList.as_view(), name='streamlist'),# api/stream/
    path('stream/<int:pk>/', StreamPlatformDetails.as_view(), name='streamdetail'), # api/stream/pk

    path('review/', ReviewDetails.as_view(), name='reviewlist'),
    path('review/<int:pk>/', ReviewList.as_view(), name='reviewdetail'), # api/review/pk
    path("stream/review/<int:pk>/", ReviewDetails.as_view(), name="reviewdetail"),
    path("stream/<int:pk>/review/", ReviewList.as_view(), name="reviewlist"),


]
