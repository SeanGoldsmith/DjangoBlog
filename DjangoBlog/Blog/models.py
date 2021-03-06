from django.db import models
from django.contrib.auth.models import User

class BlogPost(models.Model):
    post_title = models.CharField(max_length=50)
    post_date = models.DateField(auto_now_add=True)
    post_text = models.TextField()
    post_img = models.ImageField(upload_to='img', height_field=None, width_field=None, max_length=None, blank=False, null=True)

    class Meta:
        get_latest_by = 'post_date'

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blog_post = models.ForeignKey(BlogPost,on_delete=models.CASCADE)
    comment_date = models.DateTimeField()
    comment_body = models.TextField()

    class Meta:
        get_latest_by = 'comment_date'


