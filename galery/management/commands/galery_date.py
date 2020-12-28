# -*- coding: utf-8 -*-
import os       # for work with filesystem
import cv2      # image container reader

from django.conf import settings
import os

from PIL import Image, ImageDraw, ExifTags

#from datetime import date
import datetime

# IMPORT DJANGO STUFF
from django.core.files import File	# for file opening

#from django.core.exceptions import MultipleObjectsReturned

from django.core.management.base import BaseCommand, CommandError

from galery.models import Galery

class Command(BaseCommand):
    help = "Create thumbnails for galerija"
    def handle(self, *args, **options):

#        path = "/var/www/svabwilla.svabis.eu/media/"
        images = Galery.objects.all()

        for obj in images:
#            obj.galery_thumb = None
#            obj.save()
#            continue

            open_image = open(settings.MEDIA_ROOT + str(obj.galery_img), "rb")
            image_file = File(open_image)

            infile = settings.MEDIA_ROOT + str(obj.galery_img)
            im = Image.open(infile)
            exif = im.getexif()
            date = exif.get(36867)

            if date != None:

               #2018:06:17 23:38:09
                d = date.split(":")
                img_date = datetime.date( int(d[0]), int(d[1]), int(d[2].split(" ")[0]) )
#                print( obj.galery_date )
                obj.galery_date = img_date
                obj.save()

