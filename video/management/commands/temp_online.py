# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError

import os
from datetime import datetime
from video.models import Camera_online

# COMAND BEGIN
class Command(BaseCommand):
  def handle(self, *args, **options):

   # array for Camera statuses
    temp = []

    cameras = Camera_online.objects.all()
    for c in cameras:
        c.delete()
