# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError
from django.core.files import File

from video.models import Camera, Video # import models

from datetime import datetime
from time import sleep
import os, json

import re

media = "/var/www/svabis.eu/media/"
task_folder = "/home/alex/skripti/video/"
error = []

# COMAND BEGIN
class Command(BaseCommand):
    def handle(self, *args, **options):
        print( "start" )
        print( datetime.now() )

        error = []
        count = 0
        for v in Video.objects.all().order_by("-video_date"):
            count += 1

            temp_filename = str(v.video_file).split("/")[-1]
            print( temp_filename )

           # TEST VIDEO FOR ERRORS
            temp = os.system( "ffmpeg -v error -i " + media + str(v.video_file) + " -f null - 2>>error.log" )
            if temp != 0:
                print( temp )
                error.append( [v.video_file, temp_filename] )
               # !!! DELETE !!!
                v.delete()

         # stop iterations
#            if count == 10:
#                break

        print( "===================================================================================" )
        for e in error:
            print( e )
        print()
