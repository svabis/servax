# -*- coding: utf-8 -*-
from django.contrib import admin
from login.models import User_data

from .models import MapPlot, MapPlotCity


class MapPlotCityAdmin(admin.ModelAdmin):
    fields = ['name']
#    list_filter = ['name']
    list_display = ['name']

class MapPlotAdmin(admin.ModelAdmin):
#    fields = ['date', 'mark', 'lat', 'lon', 'radio', 'chk_1', 'chk_2', 'chk_3']
#    list_filter = ['date', 'radio', 'chk_1', 'chk_2', 'chk_3']
#    list_display = ['date', 'mark', 'lat', 'lon', 'radio', 'chk_1', 'chk_2', 'chk_3']
    fields = ['date', 'deleted', 'mark', 'unique', 'city', 'lat', 'lon', 'radio', 'chk_1', 'chk_2', 'chk_3']
    list_filter = ['date', 'city_id', 'deleted', 'unique', 'radio', 'chk_1', 'chk_2', 'chk_3']
    list_display = ['date', 'deleted', 'mark', 'unique', 'city', 'lat', 'lon', 'radio', 'chk_1', 'chk_2', 'chk_3']


admin.site.register(MapPlotCity, MapPlotCityAdmin)
admin.site.register(MapPlot, MapPlotAdmin)

