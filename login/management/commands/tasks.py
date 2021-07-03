# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError
from django.core.files import File

from django.utils import timezone

# import models
from video.models import Camera, Video
from login.models import Server_Task

from datetime import datetime, date
import os

#import unicodedata


media = "/var/www/svabis.eu/media/"
home_folder = "/home/"
task_folder = "/home/alex/skripti/video/tasks/"

# SET True for console output
DEBUG = False
#DEBUG = True

console_out = ""
if DEBUG == False:
  console_out = " > /dev/null 2>&1 || true"


# JSON SERIALIZER datetime NO ERROR
#def default(o):
#    if isinstance(o, (date, datetime)):
#        return o.isoformat()


# COMAND BEGIN
class Command(BaseCommand):
    def handle(self, *args, **options):
        task = Server_Task.objects.filter( task_wait = True, task_type = "imgtovid" )

       # There are no need to run outsorce
        if task.count() == 0:
            return
       # There are active tasks
        else:
            if DEBUG:
                print( "start" )
                print( datetime.now() )

       # Iterate tasks
        for t in task:
            if DEBUG:
                print( t )
                print( datetime.now() )

           # DO THE TASK
            try:
                os.system('cat ' + home_folder + t.task_input + '*.jpg | ffmpeg -f image2pipe -i - ' + task_folder + t.task_output + console_out)
            except:
                pass

           # TASK - OK
            if os.path.exists( task_folder + t.task_output ):
               # If file already exists TASK
                try:
                    obj = Video.objects.get(video_name = t.task_output)
                   # UPDATE TASK ENTRY
                    t.task_wait = False
                    t.task_done = False
                    t.save()

               # Create new Video object
                except:
                    try:
                         # GET KAMERA
                          c = Camera.objects.get( cam_user = t.task_input.split("/")[0] ) #t.task_object )
                         # SET DATE
                          new_date = datetime( int(t.task_output[0:4]), int(t.task_output[4:6]), int(t.task_output[6:8]) )
                         # GET VIDEO FILE
                          open_file = open( task_folder + t.task_output, 'rb')
                          temp_file = File(open_file)
                          new_video = Video( video_name = t.task_output, video_date = new_date, video_cam = c, video_file = temp_file)
                          new_video.save()
                         # CLEANUP RECIEVED FILE
                          os.remove(task_folder + t.task_output)
                         # UPDATE TASK ENTRY
                          t.task_wait = False
                          t.task_done = True
                          t.task_done_time = timezone.now()
                          t.save()
                    except:
                        try:
                           # CLEANUP RECIEVED FILE
                            os.remove(task_folder + t.task_output)
                        except:
                            pass
                        if DEBUG:
                            print( "!!!!! SOMETHING WENT WRONG CREATING VIDEO MODEL !!!!!" )
                            print( datetime.now() )

           # TASK FAILED - output file does not exist
            else:
                try:
                   # CLEANUP RECIEVED FILE
                    os.remove(task_folder + t.task_output)
                except:
                    pass
               # UPDATE TASK ENTRY
                t.task_wait = False
                t.task_done = False
                t.save()
