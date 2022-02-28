from django.contrib import admin
from .models import *

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ("username", "email")

class ProfileAdmin(admin.ModelAdmin):
    list_display = ("id", "first_name", "last_name", "avatar")

admin.site.register(User, UserAdmin)
admin.site.register(Profile, ProfileAdmin)