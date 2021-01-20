# -*- coding: utf-8 -*-
from idea.models import Theme, Post, PostImage

from django.conf import settings


# IMPORT DJANGO STUFF
from django.core.files import File

from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    def handle(self, *args, **options):

       # Iterate Posts
        for p in Post.objects.all():
            if p.image:
                print( p.image )

                open_image = open(settings.MEDIA_ROOT + str(p.image), "rb")
                img_file = File(open_image)

                new_img = PostImage( post=p, image=img_file )
                new_img.save()
#                break
