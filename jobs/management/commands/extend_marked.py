# -*- coding: utf-8 -*-
# IMPORT DJANGO STUFF
from django.core.management.base import BaseCommand, CommandError

from jobs.models import Jobs	# import model

from datetime import date, timedelta


# COMAND BEGIN
class Command(BaseCommand):
    def handle(self, *args, **options):
       jobs = Jobs.objects.all()

       for j in jobs:
          # Marķētie darbi
           if j.marked == True:
               if isinstance( j.marked_until, date ) == True:
                   j.marked_until = date.today() + timedelta(days=30)
                   j.save()
