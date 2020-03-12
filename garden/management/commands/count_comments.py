# -*- coding: utf-8 -*-
from garden.models import Theme, Post

# IMPORT DJANGO STUFF
from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    def handle(self, *args, **options):

       # CLEAR COUNTERS
        for t in Theme.objects.all():
            t.entry_count = 0
            t.save()

       # LOWEST LEVEL TEMA'S
        themes = Theme.objects.filter( comment = True )

       # TEMU ID MASIVS
        temp = []

       # COUNT LOWER LEVEL IERAKSTS
        for t in themes:
            temp_i = Post.objects.filter( relate_to = t )
            count = temp_i.count()

            t.entry_count = count
            t.save()
            temp.append( t.id )

        print( temp )

       # ADD COUNTERS CASCADED
        while len(temp) != 0:
             new_temp = []

             print( "-----" )
             for t in temp:
                 child = Theme.objects.get( id = t )
                 print( child )
                 parent = child.parent

                 if parent != None:
                     print( parent )
                     parent.entry_count += child.entry_count
                     parent.save()
#                     if parent.parent != None:
                     new_temp.append( parent.id )

             temp = list(set(new_temp))
             print( temp )
