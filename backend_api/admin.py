from django.contrib import admin
from .models import User, UploadFiles
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list = ('name', 'email', 'password')

    admin.site.register(User)

class UploadFilesAdmin(admin.ModelAdmin):
    list = ('title', 'type', 'file', 'access_link', 'user')
    
    admin.site.register(UploadFiles)