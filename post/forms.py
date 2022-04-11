from django import forms
from post.models import Post

class blogPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','category','post']
