from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from .models import Post
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .forms import RegisterForm
from django.urls import reverse_lazy,reverse
from django.utils.text import slugify
from django.contrib.auth.mixins import UserPassesTestMixin,LoginRequiredMixin
from .forms import CommentForm
from .models import Comments
from django.http import HttpResponseRedirect

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
    
   
    
class posts(LoginRequiredMixin,ListView):
    model=Post
    ordering=['-Date']
    context_object_name='post'
    template_name='allpost.html'


class postdetail(LoginRequiredMixin,DetailView):
    data={}
    def get(self,request,slug):
        mypost = Post.objects.get(Slug=slug)
        data={
            'post':mypost,
            'comments':CommentForm(),
            'allcomments':Comments.objects.filter(post=mypost).order_by('-id')
        }
        return render(request,'postdetail.html',data)
    def post(self,request,slug):
        mypost = Post.objects.get(Slug=slug)
        mycomment = CommentForm(request.POST)
        if mycomment.is_valid():
            com = mycomment.save(commit=False)
            com.user = request.user
            com.post=mypost
            com.save()
            return HttpResponseRedirect(reverse('postdetails',args=[slug]))

        else:
            data={
                'post':mypost,
                'comments':CommentForm()
            }
            return render(request,'postdetail.html',data)


class Signup(CreateView):
    form_class = RegisterForm
    success_url=reverse_lazy('login')
    template_name='register.html'

class createPost(LoginRequiredMixin,CreateView):
    model=Post
    template_name='createpost.html'
    fields=['Title','Token','Content','Image']
    success_url=reverse_lazy('posts')
    def form_valid(self, form):
        form.instance.Author=self.request.user
        form.instance.Slug=slugify(form.instance.Title)
        return super().form_valid(form)
    
class updatePost(LoginRequiredMixin,UpdateView,UserPassesTestMixin):
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

class deletePost(LoginRequiredMixin,DeleteView,UserPassesTestMixin):
    template_name="post_confirm_delete.html"
    model=Post
    success_url=reverse_lazy('posts')
    slug_field='Slug'
    def test_func(self):
        mypost = self.get_object()
        if(self.request.user==mypost.Author):return True
        else:return False