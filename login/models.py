# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone

from django.contrib.auth.models import User

from datetime import datetime

from smhouse.models import Location


# !!!!! USER DATA - USER ACCESS RIGHTS !!!!!
class User_data(models.Model):
    class Meta():
        db_table = "login_user_data"

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

    idea = models.BooleanField( default=False )
    idea_add = models.BooleanField( default=False )

    map = models.BooleanField( default=False )

    location = models.ForeignKey( Location, null=True, blank=True, on_delete=models.CASCADE )

    def __unicode__(self):
        return u'%s' % (self.user_user)


# !!!!! LIVE VIDEO WATCH STATISTICS !!!!!
class Live_video(models.Model):
    class Meta():
        db_table = "login_live_video_log"

    user = models.ForeignKey( User, on_delete=models.CASCADE )

    mobile = models.BooleanField( default=False )
    tablet = models.BooleanField( default=False )

    device = models.CharField( max_length=200, blank=True, null=True )

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
        db_table = "login_server_tasks"

    task_type = models.CharField( max_length=30, choices=TASK_TYPES, default="imgtovid")
    task_object = models.CharField( max_length=50, null=True, blank=True )

    task_time = models.DateTimeField( null=True, blank=True )
    task_wait = models.BooleanField( default=True )

    task_done_time = models.DateTimeField( null=True, blank=True )
    task_done = models.BooleanField( default=False )

    task_input = models.CharField( max_length=50 )
    task_output = models.CharField( max_length=50 )


    def __str__(self):
        return self.task_type


