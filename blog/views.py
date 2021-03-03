from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

class IndexView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    paginate_by = 4
    
class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    
