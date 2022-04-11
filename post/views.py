from django.shortcuts import render, redirect
from post.models import Post
from post import forms as PFORM 
# Create your views here.

def home_view(request):
    return render(request, 'home/home.html')

# single blog view 
def blogs_single(request, pk):
    blog = Post.objects.get(id=pk)
    context = {
        'blog':blog,
    }
    return render(request, 'blog/single_blog_view.html', context)

def blog_post_view(request):
    blog_post_form = PFORM.blogPostForm()
    if request.method == 'POST':
        blog_post_form = PFORM.blogPostForm(request.POST)
        if blog_post_form.is_valid():
            blog_obj = blog_post_form.save(commit=False)
            blog_obj.author = request.user
            blog_obj.save()
            return redirect('/')
    context = {
        'blog_post_form':blog_post_form,
    }
    return render(request, 'blog/blog_post.html', context)