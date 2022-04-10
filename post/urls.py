from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from post.views import home_view

urlpatterns = [
    path('1', home_view, name='one'),
]