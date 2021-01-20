# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import SuperTheme, Theme, Post, PostImage


class ThemeAdmin(admin.ModelAdmin):
# IF REMARK IS REMOVED --> ADMIN CRASHES
#    prepopulated_fields = ['slug': ('title')]
    list_display = ['relate_to_super', 'parent', 'comment', 'title', 'slug', 'created_by', 'created_date', 'last_entry', 'entry_count']
    list_filter = ['last_entry', 'comment', 'relate_to_super', 'created_by', 'created_date']


class SuperThemeAdmin(admin.ModelAdmin):
#    prepopulated_fields = {'slug': ('title',),}
    list_display = ['order', 'title', 'slug', 'icon',]


class PostAdmin(admin.ModelAdmin):
    list_display = ['relate_to', 'user', 'date', 'text_short', 'url']
    list_filter = ['date']


class PostImageAdmin(admin.ModelAdmin):
    list_display = ['post', 'image',]


admin.site.register(SuperTheme, SuperThemeAdmin)
admin.site.register(Theme, ThemeAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(PostImage, PostImageAdmin)
