from django.shortcuts import render
from post.models import Post
# Create your views here.

def home_view(request):
    return render(request, 'home/home.html')

# single blog view 
def blogs_single(request, pk):
    blog = Post.objects.get(id=pk)
    context = {
        'blog':blog,
    }
    return render(request, 'blog/single_blog.html', context)