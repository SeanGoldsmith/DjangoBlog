from django.forms import ModelForm
from django import forms
from .models import BlogPost, Comment
class PostForm(ModelForm):
    class Meta:
        model = BlogPost
        fields = '__all__'

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'
        widgets = {
            'user': forms.HiddenInput,
            'blog_post': forms.HiddenInput,
            'comment_date': forms.HiddenInput,
        }
