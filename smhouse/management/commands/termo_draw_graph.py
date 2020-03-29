# -*- coding: utf-8 -*-
from __future__ import division
from datetime import datetime

from django.core.management.base import BaseCommand, CommandError
from smhouse.termo_draw import draw_termo

# command
class Command(BaseCommand):
    help = "Draw images"
    def handle(self, *args, **options):
       # Time now
        now = datetime.now().hour
#        print( now )
        if now == 0:
           # Draw Termo week
            draw_termo("ktc", 168, 7, "%d", 2, True)
            draw_termo("ktc", 168, 7, "%d", 2, False)
            draw_termo("ktc", 168, 7, "%d", 2, None)

           # Draw Termo month
            draw_termo("ktc", 720, 30, "%d", 2, True)
            draw_termo("ktc", 720, 30, "%d", 2, False)
            draw_termo("ktc", 720, 30, "%d", 2, None)

           # Draw Termo year
#            draw_termo("ktc", 8760, 12, "%m", 3, True)
#            draw_termo("ktc", 8760, 12, "%m", 3, False)
#            draw_termo("ktc", 8760, 12, "%m", 3, None)

           # Draw 9 months
            draw_termo("ktc", 6480, 9, "%m", 3, True)
            draw_termo("ktc", 6480, 9, "%m", 3, False)
            draw_termo("ktc", 6480, 9, "%m", 3, None)

        if now == 12:
           # Draw Termo week
            draw_termo("ktc", 168, 7, "%d", 2, True)
            draw_termo("ktc", 168, 7, "%d", 2, False)
            draw_termo("ktc", 168, 7, "%d", 2, None)
