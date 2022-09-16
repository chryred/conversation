from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin
from .models import (Group, Menu, MenuAuth)


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = (
        'group_id',
        'group_nm',
        'group_desc',
        'ord_seq',
        'use_yn',
    )


@admin.register(Menu)
class MenuAdmin(DraggableMPTTAdmin):
    list_display = (
        'tree_actions',
        'tree_id',
        'lft',
        'parent',
        'indented_title',
        'menu_id',
        'menu_nm',
        'icon',
        'menu_url',
        'level',
        'ord_seq',
        'use_yn',
    )
    mptt_level_indent = 5


@admin.register(MenuAuth)
class MenuAuthAdmin(admin.ModelAdmin):
    list_display = (
        'menu',
        'group',
    )
