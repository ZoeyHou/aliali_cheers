from django.contrib import admin
from .models import Picture, Video, Catagory, Video_Comment

class PictureAdmin(admin.ModelAdmin):
    list_display = ['user', 'upload_time']

admin.site.register(Picture, PictureAdmin)

class VideoAdmin(admin.ModelAdmin):
    list_display = ['user', 'video', 'upload_time']

admin.site.register(Video, VideoAdmin)

class CatagoryAdmin(admin.ModelAdmin):
    list_display = ['catagory_name']

admin.site.register(Catagory, CatagoryAdmin)

class Video_CommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'video', 'create_time']

admin.site.register(Video_Comment, Video_CommentAdmin)
