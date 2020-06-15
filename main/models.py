from django.db import models
from django.utils import timezone
from embed_video.fields import EmbedVideoField
from django.contrib.auth.models import User

class Courses(models.Model):
    id = models.AutoField(primary_key = True)
    title = models.CharField(max_length= 50)
    category = models.CharField(max_length= 50)
    subCategory = models.CharField(max_length= 50)
    desc = models.CharField(max_length=500, default="")
    pubDate = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to="guitar/images", default="default.png")

    def __str__(self):
        return self.title

class Video(models.Model):
    v_id = models.AutoField(primary_key = True)
    v_title = models.CharField(max_length= 50)
    v_category = models.CharField(max_length= 50)
    v_desc = models.CharField(max_length=500, default="")
    v_pubDate = models.DateTimeField(default=timezone.now)
    v_video = EmbedVideoField(blank=True)

    def __str__(self):
        return self.v_title


#comment model
class Comment(models.Model):
    post = models.ForeignKey(Video,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=100, default="")
    body = models.TextField()
    created_on = models.DateTimeField(default=timezone.now)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.active)

