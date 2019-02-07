from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from Blog.models import BlogPost
def HomePage(request):

    latest_post = BlogPost.objects.latest()

    context = {
        'Post': latest_post
    }
    template = loader.get_template('./home/home.html')
    return HttpResponse(template.render(context))
