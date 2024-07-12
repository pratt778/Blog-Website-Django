from django.urls import path,include
from .views import *;
urlpatterns = [
 path('',home.as_view(),name="home"),
 path('posts/',posts,name="posts"),
 path('posts/<slug:slug>',postdetail.as_view(),name="postdetails")
]
