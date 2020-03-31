# -*- coding: utf-8 -*-
from django.contrib import admin
from smhouse.models import ElConsumption, LedTimer, Location, TermoPlace, TermoReading


# Elecrticity
class ElConsumptionAdmin(admin.ModelAdmin):
    list_display = [ 'date', 'read', 'cons', 'days', 'cons_days' ]

# Led
class LedTimerAdmin(admin.ModelAdmin):
    list_display = [ 'time', 'days', 'color', 'bright', 'effect' ]

# Location
class LocationAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('adress',), }
    list_display = [ 'adress', 'order', 'slug' ]

# Temperature
class TermoPlaceAdmin(admin.ModelAdmin):
    list_display = [ 'place', 'order', 'where', 'ambient', 'color', 'filename', 'regex' ]
    list_filter = [ 'where', 'ambient' ]

class TermoReadingAdmin(admin.ModelAdmin):
    list_display = [ 'date', 'temp', 'humy', 'place' ]
    list_filter = [ 'date', 'place' ]


admin.site.register(ElConsumption, ElConsumptionAdmin)
admin.site.register(LedTimer, LedTimerAdmin)

admin.site.register(Location, LocationAdmin)

admin.site.register(TermoPlace, TermoPlaceAdmin)
admin.site.register(TermoReading, TermoReadingAdmin)
