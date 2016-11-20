#coding:utf-8
from __future__ import unicode_literals

from django.db import models
from Authentication.models import User
from django.conf import settings

class Catagory(models.Model):
    catagory_name = models.CharField(max_length=1024)
    def __unicode__(self):
        return self.catagory_name

class Picture(models.Model):
    user = models.ForeignKey(User, related_name='User_Picture')
    img = models.ImageField(upload_to='pictures/', null=True)
    upload_time = models.DateField('上传时间', auto_now=True)

class Video(models.Model):
    user = models.ForeignKey(User, related_name='User_Video')
    video = models.FileField(upload_to='videos/')
    barrage = models.FileField(upload_to='barrages/', null=True, default=None)
    upload_time = models.DateField('上传时间', auto_now=True)
    title = models.CharField(max_length=2048)
    cover = models.ImageField(upload_to='videos/cover/')
    catagory = models.ForeignKey(Catagory, related_name='Catagory_Video')
    discription = models.TextField(max_length=2048)
    like = models.IntegerField(default=0)
    dislike = models.IntegerField(default=0)

    def __unicode__(self):
        return self.video.url.split('/')[-1]

class Video_Comment(models.Model):
    video = models.ForeignKey(Video, related_name="Video_Comment")
    user = models.ForeignKey(User, related_name="User_Comment")
    content = models.TextField(max_length=4096)
    create_time = models.TimeField('发布时间', auto_now=True)
    like = models.IntegerField(default=0)


