# -*- coding: utf-8 -*-
from __future__ import division
from datetime import datetime

from django.core.management.base import BaseCommand, CommandError
from smhouse.termo_draw import draw_termo

from smhouse.models import Location

# command
class Command(BaseCommand):
    help = "Draw images"
    def handle(self, *args, **options):
       # Time now
        now = datetime.now().hour
        for a in Location.objects.all():

            if True:
               # Draw Termo day
                print(a.slug, "day")
                draw_termo(a.slug, 24, 24, "%H", 1, "day", True)
                draw_termo(a.slug, 24, 24, "%H", 1, "day", False)
                draw_termo(a.slug, 24, 24, "%H", 1, "day", None)

            if now == 0:
               # Draw Termo week
                print(a.slug, "week")
                draw_termo(a.slug, 168, 7, "%d", 2, "week", True)
                draw_termo(a.slug, 168, 7, "%d", 2, "week", False)
                draw_termo(a.slug, 168, 7, "%d", 2, "week", None)

               # Draw Termo month
                print(a.slug, "month")
                draw_termo(a.slug, 720, 30, "%d", 2, "month", True)
                draw_termo(a.slug, 720, 30, "%d", 2, "month", False)
                draw_termo(a.slug, 720, 30, "%d", 2, "month", None)

               # Draw 6 months
                draw_termo(a.slug, 2880, 4, "%m", 3, "rand", True)
                draw_termo(a.slug, 2880, 4, "%m", 3, "rand", False)
                draw_termo(a.slug, 2880, 4, "%m", 3, "rand", None)

               # Draw 9 months
#                draw_termo(a.slug, 6480, 9, "%m", 3, "rand", True)
#                draw_termo(a.slug, 6480, 9, "%m", 3, "rand", False)
#                draw_termo(a.slug, 6480, 9, "%m", 3, "rand", None)

               # Draw 1 year
#                print(a.slug, "rand")
#                draw_termo(a.slug, 8640, 12, "%m", 3, "rand", True)
#                draw_termo(a.slug, 8640, 12, "%m", 3, "rand", False)
#                draw_termo(a.slug, 8640, 12, "%m", 3, "rand", None)

            if now == 12:
               # Draw Termo week
                print(a.slug, "week")
                draw_termo(a.slug, 168, 7, "%d", 2, "week", True)
                draw_termo(a.slug, 168, 7, "%d", 2, "week", False)
                draw_termo(a.slug, 168, 7, "%d", 2, "week", None)
