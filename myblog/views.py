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
   
    
def posts():
    pass
class postdetail(DetailView):
    template_name='postdetail.html'
    model=Post
    slug_field = 'Slug'
    context_object_name="post"
