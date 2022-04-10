from django.shortcuts import render, redirect
from post.models import Post
# Create your views here.

# all blogs on home page 
def home_view(request):
    blogs = Post.objects.all()
    context = {
        'blogs':blogs,
    }
    return render(request, 'home/home.html', context)

def afterlogin_view(request):
    return redirect('/')