# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError
from django.core.files import File

#from django.core import serializers
from django.forms.models import model_to_dict

from video.models import Camera, Video # import models
from login.models import Server_Task

from datetime import datetime, date
from time import sleep
import os, json

import unicodedata


media = "/var/www/svabwilla.svabis.eu/media/"
home_folder = "/home/"
task_folder = "/home/alex/skripti/video/tasks/"

# SET True for console output
DEBUG = False
#DEBUG = True

console_out = ""
if DEBUG == False:
  console_out = " > /dev/null 2>&1 || true"




# JSON SERIALIZER datetime NO ERROR
def default(o):
    if isinstance(o, (date, datetime)):
        return o.isoformat()


# COMAND BEGIN
class Command(BaseCommand):
  def handle(self, *args, **options):
    task = Server_Task.objects.filter( task_wait = True, task_type = "imgtovid" )

   # There are no need to run outsorce
    if task.count() == 0:
      return
   # There are active tasks
    else:
      os.system("/home/alex/skripti/etherwake.py" + console_out)
      sleep(10)
      if DEBUG:
        print( "start" )
        print( datetime.now() )

      jsfile = task_folder + "result.json"
      stat = os.stat( jsfile ) # stat <-- file parameter object
      date = datetime.fromtimestamp( stat.st_ctime ) # file creation time
      c_date = datetime.fromtimestamp( stat.st_ctime ) # file creation time

    for t in task:
      if DEBUG:
        print( datetime.now() )

     # CREATE TASK
      dict_obj = model_to_dict( t )
      task_json = json.dumps( dict_obj, sort_keys=True, indent=1, default=default )
      if DEBUG:
        print( "TASK: " + task_json )

     # SEND OBJECT FOR PROCESSING
      os.system("scp -r " + home_folder + t.task_input + " svabis@172.16.2.132:/home/svabis/SERVER/" + console_out)

     # SEND TASK JSON COMMAND
      f = open( task_folder + "task.json", "w+" )
      f.write( task_json )
      f.close()
      os.system("scp " + task_folder + "task.json svabis@172.16.2.132:/home/svabis/SERVER/comand.json" + console_out)
      if DEBUG:
        print( "WAITING..." )

     # ===============================================================================
     # WAIT FOR RESPONSE BY CORRECT ID
      result = {"id": None}
      while str(t.id) != result["id"]:
       # CHECK STATUS
        sleep(60)
        with open( jsfile ) as f:
          result = json.load(f)

       # OUTPUT RESULT
        if DEBUG:
          file = open( jsfile, "r")
          print( "RESULT: " + file.read() )
          print( result["id"] )


     # ===============================================================================
     # OUTPUT RESULT
      file = open( jsfile, "r")
      if DEBUG:
        print( "RESULT: " + file.read() + "\n" )

      if result["task_status"] == "done":
       # If file already exists
        try:
          obj = Video.objects.get(video_name = t.task_output)
          t.task_wait = False
          t.task_status = False
          t.save()

       # Create new Video object
        except:
          try:
           # GET KAMERA
            c = Camera.objects.get( cam_user = t.task_object )
           # SET DATE
            new_date = datetime( int(t.task_output[0:4]), int(t.task_output[4:6]), int(t.task_output[6:8]) )
           # GET VIDEO FILE
            open_file = open( task_folder + t.task_output, 'rb')
            temp_file = File(open_file)
            new_video = Video( video_name = t.task_output, video_date = new_date, video_cam = c, video_file = temp_file)
            new_video.save()

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


   # CREATE SHUTDOWN TASK
    task_json = '{"task_type":"poweroff"}'

   # SEND TASK JSON COMMAND
    f = open( task_folder + "task.json", "w+" )
    f.write( task_json )
    f.close()
    os.system("scp " + task_folder + "task.json svabis@172.16.2.132:/home/svabis/SERVER/comand.json" + console_out)

