# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone

from django.contrib.auth.models import User

from datetime import datetime


# !!!!! USER DATA - USER ACCESS RIGHTS !!!!!
class User_data(models.Model):
    class Meta():
        db_table = "user_data"

    user_user = models.OneToOneField( User, related_name='u', on_delete=models.CASCADE ) # User from Django Users&Groups
    user_last_visit = models.DateTimeField( null=True, blank=True ) # FOR LAST LOG (NOT AUTORIZATION)

    video_live = models.BooleanField( default=False )
    video_live_local = models.BooleanField( default=False )
    video_archive = models.BooleanField( default=False )

    galery = models.BooleanField( default=False )
    galery_add = models.BooleanField( default=False )

    sm_electr = models.BooleanField( default=False )
    sm_termo = models.BooleanField( default=False )
    sm_led = models.BooleanField( default=False )

    job_list = models.BooleanField( default=False )
    job_add = models.BooleanField( default=False )
    job_start = models.BooleanField( default=False )
    job_cancel = models.BooleanField( default=False )
    job_fin = models.BooleanField( default=False )
    job_restart = models.BooleanField( default=False )
    job_mark = models.BooleanField( default=False )

    obj_list = models.BooleanField( default=False )
    obj_list_add = models.BooleanField( default=False )
    obj_list_edit = models.BooleanField( default=False )

    garden = models.BooleanField( default=False )
    garden_add = models.BooleanField( default=False )

    map = models.BooleanField( default=False )

    def __unicode__(self):
        return u'%s' % (self.user_user)


# !!!!! LIVE VIDEO WATCH STATISTICS !!!!!
class Live_video(models.Model):
    class Meta():
        db_table = "live_video_log"

    user = models.ForeignKey( User, on_delete=models.CASCADE )

    mobile = models.BooleanField( default=False )
    tablet = models.BooleanField( default=False )

    visit = models.DateTimeField( default=timezone.now )
    leave = models.DateTimeField( default=timezone.now )

    time = models.TimeField( blank=True, null=True )

    cookie_uuid = models.CharField( max_length = 60, default='' )

    def __str__(self):
        return str(self.user.username) + " " + self.visit.strftime( "%Y/%m/%d %H:%M" )


# !!!!! OUTSORCE SERVER TASKS !!!!!
TASK_TYPES = (
    ('poweroff', 'shut down desktop'),
    ('rescale', 'rescale'),
    ('imgtovid', 'image to video'),
    ('chkvid', 'check video integrity'),
)

class Server_Task(models.Model):
    class Meta():
        db_table = "server_tasks"

    task_type = models.CharField( max_length=30, choices=TASK_TYPES, default="imgtovid")
    task_object = models.CharField( max_length=50 )

    task_time = models.DateTimeField( null=True, blank=True )

    task_input = models.CharField( max_length=50 )
    task_output = models.CharField( max_length=50 )

    task_status = models.BooleanField( default=False )
    task_wait = models.BooleanField( default=True )

    def __str__(self):
        return self.task_type


# !!!!! MAP PLOT !!!!!
PLOT_TYPES = (
    ('red', 'sarkans'),
    ('green', 'zaļš'),
    ('blue', 'zils'),
)

class MapPlot(models.Model):
#'date', 'mark', 'lat', 'lon', 'radio', 'chk_1', 'chk_2', 'chk_3'
    class Meta():
        db_table = "map_plot_points"

    date = models.DateTimeField( default = timezone.now )

    mark = models.IntegerField( null=True, blank=True )

    lat = models.CharField( max_length=50 )
    lon = models.CharField( max_length=50 )

    radio = models.CharField( max_length=10, choices=PLOT_TYPES, default="red")

    chk_1 = models.BooleanField( default=False )
    chk_2 = models.BooleanField( default=False )
    chk_3 = models.BooleanField( default=False )

