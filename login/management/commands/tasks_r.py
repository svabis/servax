# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError
from django.core.files import File

from django.utils import timezone

from video.models import Camera, Video # import models
from login.models import Server_Task

from datetime import datetime, date
import os
#import json


media = "/var/www/svabis.eu/media/"
task_folder = "/home/alex/skripti/video/tasks/"

# SET True for console output
DEBUG = False
DEBUG = True

console_out = ""
if DEBUG:
  console_out = " > /dev/null 2>&1 || true"


# JSON SERIALIZER datetime NO ERROR
#def default(o):
#    if isinstance(o, (date, datetime)):
#        return o.isoformat()


# COMAND BEGIN
class Command(BaseCommand):
  def handle(self, *args, **options):
    task = Server_Task.objects.filter( task_wait = True, task_type = "rescale" )

   # There are no need to run outsorce
    if task.count() == 0:
      return
   # There are active tasks
    else:
      if DEBUG:
        print( "start" )
        print( datetime.now() )

    c = 0
    for t in task:
     # Process stop at count in one run
      c += 1
#      if c > 20:
#        return

      if DEBUG:
        print( datetime.now() )

      if DEBUG:
        print( "TASK: " + t.task_type + " | " + t.task_input )

      try:
        os.system("cp " + media + t.task_input + " " + task_folder + "input.mp4" + console_out)
        os.system('ffmpeg -i ' + task_folder + 'input.mp4 -vf scale=640:-1 ' + task_folder + t.task_output + console_out)
      except:
        pass

      if os.path.exists( task_folder + t.task_output ):
          temp = Video.objects.get(video_name = t.task_output)
          os.system("cp " + task_folder + t.task_output + " " + media + str(temp.video_file))

         # CLEANUP RECIEVED FILE
          try:
              os.remove(task_folder + t.task_output)
          except:
              pass
          try:
              os.remove(task_folder + "input.mp4")
          except:
              pass

          t.task_wait = False
          t.task_done = True
          t.task_done_time = timezone.now()
          t.save()

      else:
         # CLEANUP RECIEVED FILE
          try:
              os.remove(task_folder + t.task_output)
          except:
              pass
          try:
              os.remove(task_folder + "input.mp4")
          except:
              pass

          t.task_wait = False
          t.task_done = False
          t.save()
