from django.contrib import admin
from .models import User, Group


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'group',
        'use_yn',
        
    )
