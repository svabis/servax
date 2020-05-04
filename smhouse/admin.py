# -*- coding: utf-8 -*-
from django.contrib import admin
from smhouse.models import ElConsumption, LedTimer, Location, TermoPlace, TermoReading, SunData


# Elecrticity
class ElConsumptionAdmin(admin.ModelAdmin):
    list_display = [ 'date', 'read', 'cons', 'days', 'cons_days' ]

# Led
class LedTimerAdmin(admin.ModelAdmin):
    list_display = [ 'time', 'days', 'color', 'bright', 'effect' ]



# Location
class LocationAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('adress',), }
    list_display = [ 'adress', 'order', 'slug', 'sun_url', 'bw_color_log' ]

# Temperature
class TermoPlaceAdmin(admin.ModelAdmin):
    list_display = [ 'place', 'order', 'where', 'ambient', 'color', 'filename', 'regex' ]
    list_filter = [ 'where', 'ambient' ]

class TermoReadingAdmin(admin.ModelAdmin):
    list_display = [ 'date', 'temp', 'humy', 'place' ]
    list_filter = [ 'date', 'place' ]

# Sunrise & Sunset
class SunDataAdmin(admin.ModelAdmin):
    list_display = [ 'date', 'where', 'sunrise', 'sunset' ]
    list_filter = [ 'date', 'where', 'sunrise', 'sunset' ]



admin.site.register(ElConsumption, ElConsumptionAdmin)
admin.site.register(LedTimer, LedTimerAdmin)

admin.site.register(Location, LocationAdmin)

admin.site.register(TermoPlace, TermoPlaceAdmin)
admin.site.register(TermoReading, TermoReadingAdmin)

admin.site.register(SunData, SunDataAdmin)
