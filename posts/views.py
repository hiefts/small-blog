from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.contrib.auth.models import User
from .models import Post
from .forms import PostForm

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
    superuser = User.objects.filter(is_superuser=True).first()
    
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = superuser
            post.save()
            return redirect('post_list.html')
    else:
        form = PostForm()
    return render(request, 'add_post.html', {'form': form})
