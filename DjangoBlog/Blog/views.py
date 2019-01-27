from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from Blog.models import BlogPost
from django.contrib.auth.decorators import user_passes_test

def admin_check(user):
    return user.is_superuser

def index(request):
    return HttpResponse('Hello')

@user_passes_test(admin_check)
def BlogList(request):
    blogList = BlogPost.objects.all()
    template = loader.get_template('blogList.html')
    context = {
        'blogList': blogList,
    }
    return HttpResponse(template.render(context, request))
