from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

# Create your models here.

# Main category for blog post 
class Category(models.Model):
    title = models.CharField(max_length=200)
    
    def __str__(self):
        return self.title

# Blog post model 
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    slug = models.SlugField(max_length=200, blank=True, null=True)
    post = models.TextField()
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    
    def __str__(self):
        return f"{self.author} ==> {self.title}"
    
    # override save for slugify 
    def save(self, *args, **kwargs):
        original_slug = slugify(self.title)
        queryset = Post.objects.all().filter(slug__iexact=original_slug).count()

        # if title matches, then modify slug fields as title-n
        count = 1
        slug = original_slug
        while(queryset):
            slug = original_slug + '-' + str(count)
            count += 1
            queryset = Post.objects.all().filter(slug__iexact=slug).count()

        self.slug = slug
        # end modifying slug field 
        super(Post, self).save(*args, **kwargs)

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    blog= models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.TextField()
    
    def __str__(self):
        return f"{self.author}'s comment on {self.blog}"
