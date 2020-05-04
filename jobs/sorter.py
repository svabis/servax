# -*- coding: utf-8 -*-
from jobs.models import Jobs

def sort_marked_jobs():
    marked = Jobs.objects.filter(marked=True).order_by('marked_id')
   # counter
    c = 1
    for j in marked:
        j.marked_id = c
        j.save()
        c += 1
