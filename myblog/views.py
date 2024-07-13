from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from .models import Post
from django.views.generic import ListView,DetailView
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
