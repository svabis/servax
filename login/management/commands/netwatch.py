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


#dt=`date '+%d/%m/%Y_%H:%M:%S'`
#con=$( netstat -nat | grep :80 | wc -l )
#response=$(curl --write-out %{http_code} --silent --output /dev/null http://www.kuvalda.lv/gallery/)

#echo $response

#printf '%s\t%s\t%s\n' $dt $response $con >> /home/alex/net.log

