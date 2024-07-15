from django.urls import path,include
from django.contrib.auth import views as authview
from .views import *;
urlpatterns = [
 path('',home.as_view(),name="home"),
 path('posts/',posts.as_view(),name="posts"),
 path('posts/<slug:slug>',postdetail.as_view(),name="postdetails"),
 path('signup/',Signup.as_view(),name='signup'),
 path('login/',authview.LoginView.as_view(template_name='login.html'),name='login'),
 path('logout/',authview.LogoutView.as_view(next_page='home'),name='logout'),
 path('createpost/',createPost.as_view(),name="createpost"),
 path('posts/<slug:slug>/update',updatePost.as_view(),name="updatepost"),
 path('posts/<slug:slug>/delete',deletePost.as_view(),name="deletepost"),
]
