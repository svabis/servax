# -*- coding: utf-8 -*-
from django.contrib import admin

from galery.models import Galery


class GaleryAdmin(admin.ModelAdmin):
    list_display = ['galery_date', 'galery_tags', 'galery_img', 'galery_thumb', 'galery_public']
    list_filter = ['galery_date', 'galery_public']

admin.site.register(Galery, GaleryAdmin)
