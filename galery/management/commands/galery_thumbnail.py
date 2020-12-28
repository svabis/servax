# -*- coding: utf-8 -*-
import os       # for work with filesystem
import cv2      # image container reader

from django.conf import settings
import os

from PIL import Image, ImageDraw, ExifTags


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


#            print( obj )
            if not obj.galery_thumb:

                open_image = open(settings.MEDIA_ROOT + str(obj.galery_img), "rb")
                image_file = File(open_image)

                infile = settings.MEDIA_ROOT + str(obj.galery_img)
                outfile = settings.MEDIA_ROOT + "/galery/thumb/thumb.jpg"
                size = 200, 200 # THUMBNAIL MAXIMUM SIZE

                try:
                   # STANDART WAY TO CREATE THUMBNAIL FROM FILE
                    im = Image.open(infile)         # OPEN IMAGE FULL SIZE

                   # KEEP ORIENTATION
#                    for orientation in ExifTags.TAGS.keys():
#                        if ExifTags.TAGS[orientation] == 'Orientation':
#                            break
                    orientation = 274

                    try:
                        exif = dict( im._getexif().items() )
                        exif[orientation] = exif[orientation]
                    except:
                        exif[orientation] = 1

                    if exif[orientation] == 3:
                        im = im.transpose(Image.ROTATE_180)
                    if exif[orientation] == 6:
                        im = im.transpose(Image.ROTATE_270)
                    if exif[orientation] == 8:
                        im = im.transpose(Image.ROTATE_90)

                    im.thumbnail(size)              # RESIZE
                except IOError:
                   # NEW WAY TO CREATE THUMB FROM BROKEN IMAGES
                    print( 'BROKEN INPUT IMAGE, TRYING NETHOD \#2' )
                    try:
                        tempfile = cv2.imread( infile )
                        cv2.imwrite(outfile, tempfile ) # WRITE TEMPORARY FULL SIZE
                        im = Image.open( outfile )      # OPEN TEMPORARY FULL SIZE
                        im.thumbnail( size )            # RESIZE
                    except:
                        print( 'BOTH METHODS FAIL !' )
                        pass

               # SAVE TEMPORARY thumbnail FILE FOR UPLOAD TO /media/thumb/
                im.save( settings.MEDIA_ROOT + "/galery/thumb/thumb.jpg", "JPEG")
                thumb = open( settings.MEDIA_ROOT + "/galery/thumb/thumb.jpg", 'rb')
                thumb_file = File(thumb)   # create thumbnail

               # CREATE NEW galerija_thumb OBJECT
                obj.galery_thumb = thumb_file
                obj.galery_thumb.name = ("thumb.jpg")
                obj.save()      # save new object Bilde into database

                print( obj.galery_thumb )
