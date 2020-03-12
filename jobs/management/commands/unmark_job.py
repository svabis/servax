# -*- coding: utf-8 -*-
# IMPORT DJANGO STUFF
from django.core.management.base import BaseCommand, CommandError

from jobs.models import Jobs	# import model

from datetime import date


# COMAND BEGIN
class Command(BaseCommand):
    def handle(self, *args, **options):
       jobs = Jobs.objects.all()

       for j in jobs:
          # Marķētie darbi
           if j.marked == True:
               if isinstance( j.marked_until, date ) == True:
                   if j.marked_until < date.today():
                       j.marked_until = None
                       j.marked = False
                       j.marked_id = None
                       j.save()
               else:
                   j.marked = False
                   j.marked_until = None
                   j.marked_id = None
                   j.save()

           elif isinstance( j.marked_until, date ) == True:
          # nemarķētie darbi ar marķējuma datumu
               j.marked_until = None
               j.marked_id = None
               j.save()

           else:
          # nemarķētie darbi ar marķējuma id
               j.marked_until = None
               j.marked_id = None
               j.save()
