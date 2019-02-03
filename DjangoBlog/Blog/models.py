from django.db import models
from django.contrib.auth.models import User

class BlogPost(models.Model):
    post_title = models.CharField(max_length=50)
    post_date = models.DateField()
    post_text = models.TextField()

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blog_post = models.ForeignKey(BlogPost,on_delete=models.CASCADE)
    comment_date = models.DateTimeField()
    comment_body = models.TextField()


