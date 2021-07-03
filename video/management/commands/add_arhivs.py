# -*- coding: utf-8 -*-
import datetime # timedelta

from datetime import date # to test if end_date is date object

from django.core.management.base import BaseCommand, CommandError
from django.core.files import File

# import models
from video.models import Camera, Video
from login.models import Server_Task

import os, re
#from slugify import slugify

# COMAND BEGIN
class Command(BaseCommand):
    def handle(self, *args, **options):
        today = datetime.datetime.today() - datetime.timedelta(days = 1)
        today_str = str(today)[:10].replace('-', '')

        cameras = Camera.objects.all().order_by("-cam_nr")
        for c in cameras:

            input = c.cam_user + "/" + today_str + "/"
            if c.cam_subfolder is not None:
                input += str( c.cam_subfolder )

#            output = today_str + "_" + slugify(c.cam_name)[0] + ".mp4"
            output = today_str + "_" + str( c.cam_prefix ) + ".mp4"

#            new_task = Server_Task( task_object=c.cam_user, task_input=input, task_output=output )
            new_task = Server_Task( task_input=input, task_output=output )
            new_task.save()

