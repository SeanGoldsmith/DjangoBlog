from django.db import models

class BlogPost(models.Model):
    post_title = models.CharField(max_length=50)
    post_date = models.DateField()
    post_text = models.TextField()




