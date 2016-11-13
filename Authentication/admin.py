from django.contrib import admin
from . import models

class UserAdmin(admin.ModelAdmin):
    list_display = ('username','password')

admin.site.register(models.User, UserAdmin)
