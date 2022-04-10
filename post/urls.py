from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from post.views import blogs_single

urlpatterns = [
    path('<int:pk>/singleBlog', blogs_single, name='singleBlog'),
]