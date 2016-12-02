#coding:utf-8
from __future__ import unicode_literals

from django.db import models
from Authentication.models import User
from django.conf import settings

class Catagory(models.Model):
    catagory_name = models.CharField(max_length=1024)
    def __unicode__(self):
        return self.catagory_name

class Video(models.Model):
    user = models.ForeignKey(User, related_name='User_Video')
    video = models.FileField(upload_to='videos/')
    barrage = models.FileField(upload_to='barrages/', null=True, default=None)
    upload_time = models.DateField('上传时间', auto_now=True)
    title = models.CharField(max_length=512)
    cover = models.ImageField(upload_to='videos/cover/', null=True)
    catagory = models.ForeignKey(Catagory, related_name='Catagory_Video')
    discription = models.TextField(max_length=2048)
    like = models.IntegerField(default=0)
    dislike = models.IntegerField(default=0)

    def __unicode__(self):
        return self.video.url.split('/')[-1]

class Video_Comment(models.Model):
    video = models.ForeignKey(Video, related_name="Video_Comment")
    user = models.ForeignKey(User, related_name="VUser_Comment")
    content = models.TextField(max_length=4096)
    create_time = models.DateTimeField('发布时间', auto_now=True)

class Audio(models.Model):
    user = models.ForeignKey(User, related_name='User_Audio')
    audio = models.FileField(upload_to='audios/')
    upload_time = models.DateField('上传时间', auto_now=True)
    title = models.CharField(max_length=512)
    cover = models.ImageField(upload_to='audios/cover/')
    catagory = models.ForeignKey(Catagory, related_name='Catagory_Audio')
    discription = models.TextField(max_length=2048)
    like = models.IntegerField(default=0)
    dislike = models.IntegerField(default=0)
    lyric = models.FileField(upload_to='audios/lyrics')

    def __unicode__(self):
        return self.audio.url.split('/')[-1]


class Audio_Comment(models.Model):
    audio = models.ForeignKey(Audio, related_name="Audio_Comment")
    user = models.ForeignKey(User, related_name="AUser_Comment")
    content = models.TextField(max_length=4096)
    create_time = models.DateTimeField('发布时间', auto_now=True)


class Picture(models.Model):
    user = models.ForeignKey(User, related_name='User_Picture')
    picture = models.ImageField(upload_to='pictures/')
    upload_time = models.DateField('上传时间', auto_now=True)
    title = models.CharField(max_length=512)
    cover = models.ImageField(upload_to='pictures/cover/')
    catagory = models.ForeignKey(Catagory, related_name='Catagory_Picture')
    discription = models.TextField(max_length=2048)
    like = models.IntegerField(default=0)
    dislike = models.IntegerField(default=0)

    def __unicode__(self):
        return self.picture.url.split('/')[-1]


class Picture_Comment(models.Model):
    picture = models.ForeignKey(Picture, related_name="Picture_Comment")
    user = models.ForeignKey(User, related_name="PUser_Comment")
    content = models.TextField(max_length=4096)
    create_time = models.DateTimeField('发布时间', auto_now=True)


class Like_Item(models.Model):
    user = models.ForeignKey(User, related_name="Like_User")
    picture = models.ForeignKey(Picture, related_name="Like_Picture", blank=True, null=True)
    video = models.ForeignKey(Video, related_name="Like_Video", blank=True, null=True)
    audio = models.ForeignKey(Audio, related_name="Like_Audio", blank=True, null=True)


class Dislike_Item(models.Model):
    user = models.ForeignKey(User, related_name="Dislike_User")
    picture = models.ForeignKey(Picture, related_name="Dislike_Picture", blank=True, null=True)
    video = models.ForeignKey(Video, related_name="Dislike_Video", blank=True, null=True)
    audio = models.ForeignKey(Audio, related_name="Dislike_Audio", blank=True, null=True)


class Collect_Item(models.Model):
    user = models.ForeignKey(User, related_name="Collect_User")
    picture = models.ForeignKey(Picture, related_name="Collect_Picture", blank=True, null=True)
    video = models.ForeignKey(Video, related_name="Collect_Video", blank=True, null=True)
    audio = models.ForeignKey(Audio, related_name="Collect_Audio", blank=True, null=True)
