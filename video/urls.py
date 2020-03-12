# -*- coding: utf-8 -*-
from django.conf.urls import include, url

from video.views import live, stream, archive_main, leave_video, all_cam_on


urlpatterns = [
# LIVE VIDEO
    url(r'^live/$', live),
    url(r'^stream/$', stream),

# Leave LIVE VIDEO
    url(r'^exit_video/', leave_video),

# FORCE ALL CAMERAS ON
    url(r'^camera_on/', all_cam_on),

# ARHIVS
#    url(r'^archive/<int:date>/$', archive_main),
    url(r'^archive/$', archive_main),
]
