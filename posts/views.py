from django.shortcuts import render # need or not?
from django.views.generic import ListView, DetailView
from .models import Post

# Create your views here.
class PostListView(ListView):
    model = Post
    template_name = "post_list.html"

class PostDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"
