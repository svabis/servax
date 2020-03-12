# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError

from video.models import Camera

# COMAND BEGIN
class Command(BaseCommand):
    def handle(self, *args, **options):

        cameras = Camera.objects.all()
        for c in cameras:

            c.cam_visible = True
            c.save()
