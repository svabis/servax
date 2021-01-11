# -*- coding: utf-8 -*-
from django.utils import timezone
from django.db import models

import os
import datetime

# Create your models here.
def get_file_path(instance, filename):
   # clean filename without folder names
    filename = '/' + filename.split('/')[-1]
   # get date using string to datetime
    date = filename[1:9]
    datetime_object = datetime.datetime.strptime( date, '%Y%m%d')
   # folder name --> year_week
    folder = 'video_new/' + datetime_object.strftime('%Y_%W')
    return os.path.join('', folder + filename)


# !!!!! KAMERA !!!!!
class Camera(models.Model):
    class Meta():
        db_table = "video_cameras"
        verbose_name_plural = "Kameras"

    cam_name = models.CharField( max_length = 100 )

    cam_visible = models.BooleanField( default=True )

    cam_slug = models.SlugField( unique = True )
    cam_nr = models.IntegerField( default = 1 ) # secība iekš "Live Video"

    cam_img = models.BooleanField( default=False ) #  kameras reload ar Date palīdzību
    cam_stream = models.BooleanField( default=False ) #  kameras reload ar Date palīdzību

    cam_user = models.CharField( max_length = 50, default = 'username' )  # FTP username ( /home/****/video/ )
    cam_url = models.URLField( max_length=200, default ='http://', blank = True, null=True )       # LIVE stream  ( http:// )

    cam_url_local = models.URLField( max_length=200, default ='http://', blank = True, null=True )
    cam_url_stream = models.URLField( max_length=200, default ='http://', blank = True, null=True )

    cam_width = models.IntegerField( default = 640 )
    cam_height = models.IntegerField( default = 320 )

    cam_icon = models.CharField( max_length = 50, default = '' )
    cam_color = models.CharField( max_length = 7, default = '' )

    def __str__(self):
        return self.cam_name


# !!!!! KAMERA ONLINE !!!!!
class Camera_online(models.Model):
    class Meta():
        db_table = "video_cameras_online"
        verbose_name_plural = "Kameras onlainā"

    date = models.DateTimeField( default = timezone.now )

    cam_01 = models.BooleanField( default=False )
    cam_02 = models.BooleanField( default=False )
    cam_03 = models.BooleanField( default=False )
    cam_04 = models.BooleanField( default=False )

    def __str__(self):
        return str(self.date)


# !!!!! VIDEO !!!!!
class Video(models.Model):
    class Meta():
        db_table = "video"
        verbose_name_plural = "Videoklipi"

    video_cam  = models.ForeignKey( Camera, on_delete=models.CASCADE )
    video_name = models.CharField( max_length = 50 )
#    video_date = models.DateTimeField( default = timezone.now )
    video_date = models.DateField( default = timezone.now )
    video_file = models.FileField(upload_to = get_file_path, max_length=200, default ='' )

    def __str__(self):
        return 'Video: ' + self.video_name


# !!!!! VIDEO DAY COMMENT !!!!!
class VideoDayComment(models.Model):
    class Meta():
        db_table = "video_day_comment"
        verbose_name_plural = "Video arhīva dienu komentāri"

    date = models.DateField( default = timezone.now )

    time = models.DateTimeField( null=True, blank=True )

    comment = models.CharField( max_length = 250 )

    def __str__(self):
        return 'Comment: ' + self.comment
