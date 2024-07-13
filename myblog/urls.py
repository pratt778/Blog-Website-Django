from django.urls import path,include
from .views import *;
urlpatterns = [
 path('',home.as_view(),name="home"),
 path('posts/',posts.as_view(),name="posts"),
 path('posts/<slug:slug>',postdetail.as_view(),name="postdetails")
]
