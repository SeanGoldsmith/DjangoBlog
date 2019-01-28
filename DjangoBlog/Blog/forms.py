from django.forms import ModelForm
from .models import BlogPost
class PostForm(ModelForm):
    class Meta:
        model = BlogPost
        fields = '__all__'