from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from .models import Post
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .forms import RegisterForm
from django.urls import reverse_lazy
from django.utils.text import slugify
from django.contrib.auth.mixins import UserPassesTestMixin
# Create your views here.
class home(ListView):
    model=Post
    ordering=["-Date"]
    context_object_name='post'
    template_name='index.html'

    def get_queryset(self):
        query= super().get_queryset()
        data=query[:2]
        return data
    
   
    
class posts(ListView):
    model=Post
    ordering=['-Date']
    context_object_name='post'
    template_name='allpost.html'


class postdetail(DetailView):
    template_name='postdetail.html'
    model=Post
    slug_field = 'Slug'
    context_object_name="post"

class Signup(CreateView):
    form_class = RegisterForm
    success_url=reverse_lazy('login')
    template_name='register.html'

class createPost(CreateView):
    model=Post
    template_name='createpost.html'
    fields=['Title','Token','Content','Image']
    success_url=reverse_lazy('posts')
    def form_valid(self, form):
        form.instance.Author=self.request.user
        form.instance.Slug=slugify(form.instance.Title)
        return super().form_valid(form)
    
class updatePost(UpdateView,UserPassesTestMixin):
    model=Post
    template_name='updatepost.html'
    success_url=reverse_lazy('posts')
    slug_field='Slug'
    fields=['Title','Token','Content','Image']

    def test_func(self):
        mypost = self.get_object
        if self.reqeust.user == mypost.Author:
            return True
        else:return False

class deletePost(DeleteView,UserPassesTestMixin):
    template_name="post_confirm_delete.html"
    model=Post
    success_url=reverse_lazy('posts')
    slug_field='Slug'
    def test_func(self):
        mypost = self.get_object()
        if(self.request.user==mypost.Author):return True
        else:return False