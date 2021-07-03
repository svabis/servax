# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError

import os
from datetime import datetime
from video.models import Camera, Camera_online

# COMAND BEGIN
class Command(BaseCommand):
  def handle(self, *args, **options):

   # array for Camera statuses
    temp = []

    cameras = Camera.objects.all().order_by('cam_nr')
    for c in cameras:
      print( "=========================================================" )
      print( c.cam_name )
      response = os.system("ping -c 1 " + c.cam_url_local.split("/")[2])
      if response == 0:
        c.cam_visible = True
#        print( c.cam_name )
#        print( c.cam_visible )
        temp.append(True)
      else:
        c.cam_visible = False
#        print( c.cam_nos )
#        print( c.cam_visible )
        temp.append(False)
      c.save()
      print( "" )

#    print( c )
    new_online = Camera_online( cam_01 = temp[0], cam_02 = temp[1], cam_03 = temp[2], cam_04 = temp[3], cam_05 = temp[4] )
    new_online.save()
