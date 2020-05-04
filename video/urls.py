# -*- coding: utf-8 -*-
from django.conf.urls import include, url

from video import views


urlpatterns = [
# JSON for notification if user is watching online
    url(r'^online/$', views.notificator),

# LIVE VIDEO
    url(r'^live/$', views.live),
    url(r'^stream/$', views.stream),

# Leave LIVE VIDEO
    url(r'^exit_video/', views.leave_video),

# FORCE ALL CAMERAS ON
    url(r'^camera_on/', views.all_cam_on),

# ARHIVS
#    url(r'^archive/<int:date>/$', views.archive_main),
    url(r'^archive/$', views.archive_main),
]
