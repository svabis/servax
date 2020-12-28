# -*- coding: utf-8 -*-
import os       # for work with filesystem
import cv2      # image container reader
from PIL import Image, ImageDraw, ExifTags


# IMPORT DJANGO STUFF
from django.core.files import File	# for file opening

#from django.core.exceptions import MultipleObjectsReturned

from django.core.management.base import BaseCommand, CommandError

from jobs.models import JobObj_image

class Command(BaseCommand):
    help = "Create thumbnails for jobs objects"
    def handle(self, *args, **options):

        path = "/var/www/svabis.eu/media/"
        bildes = JobObj_image.objects.all()

        for obj in bildes:
#            obj.obj_image_small = None
#            obj.save()
#            continue

            if not obj.obj_image_small:

                open_image = open(path + str(obj.obj_image_big), "rb")
                image_file = File(open_image)

                infile = path + str(obj.obj_image_big)
                outfile = "/var/www/svabis.eu/media/temp.jpg"
                size = 100, 100 # THUMBNAIL MAXIMUM SIZE

                try:
                   # STANDART WAY TO CREATE THUMBNAIL FROM FILE
                    im = Image.open(infile)         # OPEN IMAGE FULL SIZE

                   # KEEP ORIENTATION
                    for orientation in ExifTags.TAGS.keys():
                        if ExifTags.TAGS[orientation] == 'Orientation':
                            break

                    try:
                        exif = dict( im._getexif().items() )
#                        print( exif[orientation] )
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

#                continue
               # SAVE TEMPORARY thumbnail FILE FOR UPLOAD TO /media/thumb/
                im.save( "/var/www/svabis.eu/media/job_obj/temp.jpg", "JPEG")
                thumb = open( "/var/www/svabis.eu/media/job_obj/temp.jpg", 'rb')
                thumb_file = File(thumb)   # create thumbnail

               # CREATE NEW OBJECT Image
                obj.obj_image_small = thumb_file
                obj.obj_image_small.name = ("thumb.jpg")
                obj.save()      # save new object Bilde into database

                print( obj.obj_image_small )
