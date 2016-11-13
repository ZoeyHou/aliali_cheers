#coding:utf-8
from __future__ import unicode_literals

from django.db import models
from Authentication.models import User
from django.conf import settings

class Picture(models.Model):
    user = models.ForeignKey(User, related_name='User_Picture')
    img = models.ImageField(upload_to='pictures/', null=True)
    upload_time = models.DateField('上传时间', auto_now=True)

class Video(models.Model):
    user = models.ForeignKey(User, related_name='User_Video')
    video = models.FileField(upload_to='videos/')
    upload_time = models.DateField('上传时间', auto_now=True)
    barrage = models.FileField(upload_to='barrages/', null=True, default=None)

