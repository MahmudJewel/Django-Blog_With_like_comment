from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from home.views import home_view, afterlogin_view

urlpatterns = [
    path('', home_view, name='home'),
    
    path('login', LoginView.as_view(template_name='home/login.html'), name='login'),
    path('logout', LogoutView.as_view(template_name='home/logout.html'), name='logout'),
    path('afterlogin', afterlogin_view, name='afterlogin')
]