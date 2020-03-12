# -*- coding: utf-8 -*-
import datetime # timedelta

from datetime import date # to test if end_date is date object

from django.core.management.base import BaseCommand, CommandError
from django.core.files import File

from video.models import Camera, Video # import models
from login.models import Server_Task

import os, re
from slugify import slugify

# COMAND BEGIN
class Command(BaseCommand):
  def handle(self, *args, **options):
    today = datetime.datetime.today() - datetime.timedelta(days = 1)
    today_str = str(today)[:10].replace('-', '')

    cameras = Camera.objects.all()
    for c in cameras:
      input = c.cam_user + "/" + today_str + "/"

      if c.cam_nr == 3 or c.cam_nr == 4:
        input = input + "images/"

      output = today_str + "_" + slugify(c.cam_name)[0] + ".mp4"

      new_task = Server_Task( task_object=c.cam_user, task_input=input, task_output=output )
      new_task.save()
