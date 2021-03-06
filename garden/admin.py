# -*- coding: utf-8 -*-
from django.contrib import admin
from garden.models import SuperTheme, Theme, Post


class ThemeAdmin(admin.ModelAdmin):
# IF REMARK IS REMOVED --> ADMIN CRASHES
#    prepopulated_fields = ['slug': ('title')]
    list_display = ['relate_to_super', 'parent', 'comment', 'title', 'slug', 'created_by', 'created_date', 'last_entry', 'entry_count']
    list_filter = ['last_entry', 'comment', 'relate_to_super', 'created_by', 'created_date']


class SuperThemeAdmin(admin.ModelAdmin):
#    prepopulated_fields = {'slug': ('title',),}
    list_display = ['order', 'title', 'slug']


class PostAdmin(admin.ModelAdmin):
    list_display = ['relate_to', 'user', 'date', 'text_short']
    list_filter = ['date']


admin.site.register(SuperTheme, SuperThemeAdmin)
admin.site.register(Theme, ThemeAdmin)
admin.site.register(Post, PostAdmin)
