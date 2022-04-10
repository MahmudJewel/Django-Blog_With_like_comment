from django.shortcuts import render, redirect

# Create your views here.

def home_view(request):
    return render(request, 'home/home.html')

def afterlogin_view(request):
    return redirect('/')