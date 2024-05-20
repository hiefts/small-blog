from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'description', 'content'] 

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password']
