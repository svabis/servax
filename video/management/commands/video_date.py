# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError
#from django.core.files import File

from video.models import Video # import models

from datetime import datetime, date
#from time import sleep

#import re

media = "/var/www/svabwilla.svabis.eu/media/"
task_folder = "/home/alex/skripti/video/"
error = []

# COMAND BEGIN
class Command(BaseCommand):
  def handle(self, *args, **options):
    print "start"
    print datetime.now()

    error = []
    count = 0
    for v in Video.objects.all().order_by("-video_date"):
      count += 1

      temp = str(v.video_file).split("/")[-1].split("_")[0]
      true_date = datetime( int(temp[0:4]), int(temp[4:6]), int(temp[6:8]) ).date()

      if v.video_date != true_date:
#          error.append( 1 )
          v.video_date = true_date
          v.save()

    print "==================================================================================="
#    for e in error:
#      print e
    print len( error )
