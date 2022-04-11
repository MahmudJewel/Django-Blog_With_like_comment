from django.contrib import admin
from post.models import Category, Post, Comment
# Register your models here.

lst = [Category, Post,Comment]

admin.site.register(lst)