# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError
from django.core.files import File

#from django.core import serializers
#from django.forms.models import model_to_dict

from video.models import Camera, Video # import models
from login.models import Server_Task

from datetime import datetime, date
#from time import sleep
import os
import json

#import unicodedata


media = "/var/www/svabwilla.svabis.eu/media/"
#home_folder = "/home/"
task_folder = "/home/alex/skripti/video/tasks/"

# SET True for console output
DEBUG = False
DEBUG = True

console_out = ""
if DEBUG:
  console_out = " > /dev/null 2>&1 || true"




# JSON SERIALIZER datetime NO ERROR
def default(o):
    if isinstance(o, (date, datetime)):
        return o.isoformat()


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
     # Process only 10 at one run
      c += 1
      if c > 10:
        return

      if DEBUG:
        print( datetime.now() )

      if DEBUG:
        print( "TASK: " + t )

      try:
        os.system("cp " + media + t.task_input + " " + task_folder + "input.mp4" + console_out)
        os.system('ffmpeg -i ' + task_folder + 'input.mp4 -vf scale=640:-1 ' + task_folder + t.task_output + console_out)
      except:
        pass

      if os.path.exists( task_folder + t.task_output ):
       # If file already exists
        try:
          temp = Video.objects.get(video_name = t.task_object)
          os.system("cp " + task_folder + t.task_output + " " + media + str(temp.video_file))

         # CLEANUP RECIEVED FILE
          os.remove(task_folder + t.task_output)

          t.task_wait = False
          t.task_status = True
          t.save()

        except:
          if DEBUG:
            print( "!!!!! SOMETHING WENT WRONG CREATING VIDEO FILE !!!!!" )

      else:
        t.task_wait = False
        t.task_status = False
        t.save()
