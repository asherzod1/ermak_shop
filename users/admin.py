from django.contrib import admin
from django.contrib.admin import ModelAdmin

from users.models import User, Role, Profile


# Register your models here.


@admin.register(User)
class UserAdmin(ModelAdmin):
    list_display = ('phone_number', 'first_name', 'last_name', 'username', 'email')
    list_display_links = ["phone_number"]


@admin.register(Role)
class RoleAdmin(ModelAdmin):
    list_display = ('name', )
    list_display_links = ["name"]


@admin.register(Profile)
class ProfileAdmin(ModelAdmin):
    list_display = ('id', 'user', 'role')
    list_display_links = ["id"]
