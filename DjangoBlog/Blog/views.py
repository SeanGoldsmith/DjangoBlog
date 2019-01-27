from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from Blog.models import BlogPost

def index(request):
    return HttpResponse('Hello')
def BlogList(request):
    blogList = BlogPost.objects.all()
    template = loader.get_template('blogList.html')
    context = {
        'blogList': blogList,
    }
    return HttpResponse(template.render(context, request))
