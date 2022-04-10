from django.contrib import admin
from post.models import Category, Post
# Register your models here.

lst = [Category, Post]

admin.site.register(lst)