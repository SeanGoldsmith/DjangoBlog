from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from Blog.models import BlogPost, Comment
from django.contrib.auth.decorators import user_passes_test
from .forms import PostForm, CommentForm
from datetime import datetime

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

def Post(request, post_id):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            return HttpResponse('Failed')
    else:
        blogPost = get_object_or_404(BlogPost, pk=post_id)
        comments = Comment.objects.all().filter(blog_post=blogPost)
        template = loader.get_template('blogPost.html')
        form = CommentForm(initial={'comment_date':datetime.now(),'user':request.user,'blog_post':blogPost})
        context = {
            'blogPost': blogPost,
            'form': form,
            'comments': comments,
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

