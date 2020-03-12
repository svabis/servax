from django.contrib import admin
from smhouse.models import ElConsumption, LedTimer


class ElConsumptionAdmin(admin.ModelAdmin):
    list_display = [ 'date', 'read', 'cons', 'days', 'cons_days' ]

class LedTimerAdmin(admin.ModelAdmin):
    list_display = [ 'time', 'days', 'color', 'bright', 'effect' ]

admin.site.register(ElConsumption, ElConsumptionAdmin)
admin.site.register(LedTimer, LedTimerAdmin)
