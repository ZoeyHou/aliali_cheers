from django.contrib import admin
from .models import Picture, Video

class PictureAdmin(admin.ModelAdmin):
    list_display = ['user', 'upload_time']

admin.site.register(Picture, PictureAdmin)

class VideoAdmin(admin.ModelAdmin):
    list_display = ['user', 'video', 'upload_time']

admin.site.register(Video, VideoAdmin)
