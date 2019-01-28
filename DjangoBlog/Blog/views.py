from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from Blog.models import BlogPost
from django.contrib.auth.decorators import user_passes_test
from .forms import PostForm

def admin_check(user):
    return user.is_superuser

def index(request):
    return HttpResponse('Hello')

def BlogList(request):
    blogList = BlogPost.objects.all()
    template = loader.get_template('blogList.html')
    context = {
        'blogList': blogList,
    }
    return HttpResponse(template.render(context, request))

@user_passes_test(admin_check)
def PostCreate(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            print("Success")
            form.save()
            return HttpResponseRedirect('http://localhost:8000/Blog/BlogList')
        else:
            return HttpResponse('FAILED!')
    else:
        form = PostForm()
        return render(request, 'postForm.html', {'form':form})

