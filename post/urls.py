from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from post.views import blogs_single, blog_post_view, like_view

urlpatterns = [
    path('<int:pk>/singleBlog', blogs_single, name='singleBlog'),
    path('post_Blog', blog_post_view, name='post_Blog'),
    path('<int:pk>/likeLink', like_view, name='likeLink'),
]