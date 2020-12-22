# -*- coding: utf-8 -*-
from django.contrib import admin
from login.models import User_data, Live_video, Server_Task


class User_dataAdmin(admin.ModelAdmin):
    fields = ['user_user', 'user_last_visit',
              'video_live', 'video_live_local', 'video_archive',
              'galery', 'galery_add',
              'sm_electr', 'sm_termo',  'sm_led',
              'job_list', 'job_add', 'job_mark', 'job_start', 'job_fin', 'job_cancel', 'job_restart',
              'obj_list', 'obj_list_add', 'obj_list_edit',
              'garden', 'garden_add',
              'map']

    list_display = ['user_user', 'user_last_visit',
              'video_live', 'video_live_local', 'video_archive',
              'galery', 'galery_add',
              'sm_electr', 'sm_termo', 'sm_led',
              'job_list', 'job_add', 'job_mark', 'job_start', 'job_fin', 'job_cancel', 'job_restart',
              'obj_list', 'obj_list_add', 'obj_list_edit',
              'garden', 'garden_add',
              'map']


class Live_videoAdmin(admin.ModelAdmin):
    fields = ['user', 'mobile', 'tablet', 'visit', 'leave', 'time', 'cookie_uuid']
    list_filter = ['visit', 'user', 'mobile', 'tablet']
    list_display = ['user', 'mobile', 'tablet', 'visit', 'leave', 'time', 'cookie_uuid']



class Server_TaskAdmin(admin.ModelAdmin):
    fields = ['task_type', 'task_object', 'task_time', 'task_input', 'task_output', 'task_status', 'task_wait']
    list_filter = ['task_type', 'task_time', 'task_status', 'task_wait']
    list_display = ['task_type', 'task_object', 'task_time', 'task_input', 'task_output', 'task_status', 'task_wait']


admin.site.register(User_data, User_dataAdmin)
admin.site.register(Live_video, Live_videoAdmin)
admin.site.register(Server_Task, Server_TaskAdmin)
