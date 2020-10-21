# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError
from django.core.files import File

from video.models import Video # import models

from login.models import Server_Task

import os, re
from slugify import slugify
from datetime import datetime, timedelta

media = "/var/www/svabwilla.svabis.eu/media/"

# COMAND BEGIN
class Command(BaseCommand):
  def handle(self, *args, **options):

   # Date where to start
    s_date = datetime(2019, 10, 11).date()
   # Date 2 weaks ago (end date)
    e_date = (datetime.now() - timedelta(days=7)).date()

    print( s_date )
    print( e_date )

    count = 0

    vid = Video.objects.all().order_by('video_date')
    for v in vid:

     try:
     # Get Videos in date range
      if v.video_date > s_date and v.video_date < e_date:
       # Get all "big" videos
        if v.video_file.size > 70000000:
          count += 1
#          print( v.video_file )

          t_obj = v.video_name
          print( t_obj )

          t_output = str(v.video_file).split('/')[-1]
#          print( t_output )

         # Create New Task
#          new_task = Server_Task( task_type="rescale", task_object=t_obj, task_input=v.video_file, task_output=t_output )
#          new_task.save()
     except:
       print( str(v) + " file missing" )

    print( count )
