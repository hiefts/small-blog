from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView, DetailView
from django.contrib.auth import login, logout, authenticate
from .models import Post
from .forms import PostForm, RegisterForm

# Create your views here.
class PostListView(ListView):
    model = Post
    template_name = "post_list.html"

    def get_queryset(self):
        return Post.objects.all().order_by('-pk')

class PostDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"

def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_list.html')
    else:
        form = PostForm()
    return render(request, 'add_post.html', {'form': form})

class RegisterView(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, 'registration/register.html', {'form': form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('post_list')
        return render(request, 'registration/register.html', {'form': form})
