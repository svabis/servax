# -*- coding: utf-8 -*-
from django.contrib import admin

from button.models import * #Meeting, MeetingPaticipant, MeetingButton

class MeetingAdmin(admin.ModelAdmin):
    fields = ['creator', 'date_added', 'title', 'url', 'end', 'push', 'timer']
    list_filter = ['creator', 'date_added', 'end']
    list_display = ['creator', 'date_added', 'title', 'url', 'end', 'push', 'timer']


class MeetingPaticipantAdmin(admin.ModelAdmin):
    fields = ['meeting', 'participiant', 'date_added', 'date_active', 'active']
    list_filter = ['date_added', 'date_active', 'active']
    list_display = ['meeting', 'participiant', 'date_added', 'date_active', 'active']


class MeetingButtonAdmin(admin.ModelAdmin):
    fields = ['participant', 'meeting', 'date_pushed', 'time_remaining']
    list_filter = ['meeting', 'date_pushed']
    list_display = ['participant', 'meeting', 'date_pushed', 'time_remaining']


admin.site.register(Meeting, MeetingAdmin)
admin.site.register(MeetingPaticipant, MeetingPaticipantAdmin)
admin.site.register(MeetingButton, MeetingButtonAdmin)
