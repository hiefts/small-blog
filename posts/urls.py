from django.urls import path

from .views import PostListView, PostDetailView, add_post, RegisterView, CustomLoginView, CustomLogoutView

urlpatterns = [
    path("<int:pk>/", PostDetailView.as_view(), name="post_detail"),
    path("", PostListView.as_view(), name="post_list"),
    path('add/', add_post, name='add_post'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout')
]
