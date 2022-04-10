from django.urls import path, include
from authentication.views import signup_view

urlpatterns = [
    path('signup', signup_view, name='signup'),
]