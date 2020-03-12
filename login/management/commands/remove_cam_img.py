# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError
#from django.core.files import File

from video.models import Camera
from login.models import Server_Task

import shutil

folder = "/home/"

# COMAND BEGIN
class Command(BaseCommand):
  def handle(self, *args, **options):
    cam = Camera.objects.all()
    for c in cam:
     temp = folder + c.cam_user +  "/19700101"
     try:
       shutil.rmtree( temp )
       print( temp )
     except:
       pass


    tasks = Server_Task.objects.all().order_by("-id")
    for t in tasks:
      if t.task_status == True and t.task_type == "imgtovid":
        try:
          temp = folder + t.task_input.split("/")[0] + "/" + t.task_input.split("/")[1]
          shutil.rmtree( temp )
#          print( temp )
        except:
          pass
