from django import forms
from post.models import Post, Comment

class blogPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','category','post']

class commentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']
