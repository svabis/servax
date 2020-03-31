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
            draw_termo("ktc", 168, 7, "%d", 2, "week", True)
            draw_termo("ktc", 168, 7, "%d", 2, "week", False)
            draw_termo("ktc", 168, 7, "%d", 2, "week", None)

           # Draw Termo month
            draw_termo("ktc", 720, 30, "%d", 2, "month", True)
            draw_termo("ktc", 720, 30, "%d", 2, "month", False)
            draw_termo("ktc", 720, 30, "%d", 2, "month", None)

           # Draw 9 months
            draw_termo("ktc", 6480, 9, "%m", 3, "rand", True)
            draw_termo("ktc", 6480, 9, "%m", 3, "rand", False)
            draw_termo("ktc", 6480, 9, "%m", 3, "rand", None)

        if now == 12:
           # Draw Termo week
            draw_termo("ktc", 168, 7, "%d", 2, "week", True)
            draw_termo("ktc", 168, 7, "%d", 2, "week", False)
            draw_termo("ktc", 168, 7, "%d", 2, "week", None)
