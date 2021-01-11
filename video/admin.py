# -*- coding: utf-8 -*-
from django.contrib import admin
from video.models import Camera, Camera_online, Video, VideoDayComment


class CameraAdmin(admin.ModelAdmin):
    prepopulated_fields = {'cam_slug': ('cam_name',),}
    fields = ['cam_name', 'cam_slug',
              'cam_visible', 'cam_nr',
              'cam_user', 'cam_url', 'cam_url_local', 'cam_url_stream',
              'cam_width', 'cam_height',
              'cam_img', 'cam_stream',
              'cam_icon', 'cam_color']
    list_display = ['cam_name', 'cam_visible', 'cam_nr', 'cam_user', 'cam_url', 'cam_url_local', 'cam_url_stream', 'cam_width', 'cam_height', 'cam_img', 'cam_stream', 'cam_icon', 'cam_color']

class Camera_onlineAdmin(admin.ModelAdmin):
    list_filter = ['date']
    list_display = ['date', 'cam_01', 'cam_02','cam_03','cam_04']

class VideoAdmin(admin.ModelAdmin):
    list_filter = ['video_date', 'video_cam']
    list_display = ['video_name', 'video_date', 'video_cam', 'video_file']


class VideoDayCommentAdmin(admin.ModelAdmin):
    list_filter = ['date']
    list_display = ['date', 'time', 'comment']



admin.site.register(Camera, CameraAdmin)
admin.site.register(Camera_online, Camera_onlineAdmin)
admin.site.register(Video, VideoAdmin)

admin.site.register(VideoDayComment, VideoDayCommentAdmin)
