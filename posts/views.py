from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, View
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from .models import Post
from .forms import PostForm, UserRegistrationForm

# Create your views here.
class PostListView(ListView):
    model = Post
    template_name = "post_list.html"

    def get_queryset(self):
        return Post.objects.all().order_by('-pk')

class PostDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"

def add_post(LoginRequiredMixin, View, request):
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
        form = UserRegistrationForm()
        return render(request, 'register.html', {'form': form})
    
    def post(self, request):
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('post_list.html')
        return render(request, 'register.html', {'form': form})

class CustomLoginView(LoginView):
    template_name = 'login.html'

class CustomLogoutView(LogoutView):
    template_name = 'logged_out.html'
