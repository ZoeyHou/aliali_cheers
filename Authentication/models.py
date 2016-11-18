from __future__ import unicode_literals

from django.db import models

class User(models.Model):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)
    face1 = models.ImageField(upload_to="faces/", null=True)
    face2 = models.ImageField(upload_to="faces/", null=True)
    face3 = models.ImageField(upload_to="faces/", null=True)

    def __unicode__(self):
        return self.username


