from django.urls import path

from .views import PostListView, PostDetailView, add_post

urlpatterns = [
    path("<int:pk>/", PostDetailView.as_view(), name="post_detail"),
    path("", PostListView.as_view(), name="post_list"),
    path('add/', add_post, name='add_post'),
]
