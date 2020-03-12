# -*- coding: utf-8 -*-
#from django.shortcuts import render, redirect

#from jobs.models import Jobs		# import aplication models

#from login.models import User_data

#from main.args import create_args

from datetime import datetime, date, timedelta
#import itertools	# Nested Counter


# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! SORT CHOISES START !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# JOBS START
def sort1(job):
    today = date.today()
    oldestDate = job.order_by('jobs_date_added')[0].jobs_date_added
    listEnd = True

    jobs = []
    d = 0 # day counter
    while (listEnd):
        try:
            dj = job.filter(jobs_date_added__startswith=( today - timedelta( days=d ))) #.order_by('-jobs_date_added')
            if dj.count() != 0:
                jobs.append(dj)
        except: # if day is empty
            pass
        if today - timedelta( days=d ) == oldestDate:
            listEnd = False
        d += 1 # increase day counter
    return jobs

def sort2(job):
    today = date.today()
    oldestDate = job.order_by('jobs_date_added')[0].jobs_date_added
    listEnd = True

    jobs = []
    d = 0 # day counter
    while (listEnd):
        try:
            dj = job.filter(jobs_date_added__startswith=( oldestDate + timedelta( days=d ))) #.order_by('jobs_date_added')
            if dj.count() != 0:
                jobs.append(dj)
        except: # if day is empty
            pass
        if oldestDate + timedelta( days=d ) == today:
            listEnd = False
        d += 1 # increase day counter
    return jobs

# JOBS START
def sort3(job):
        return job.order_by('jobs_date_start').exclude(jobs_date_start__isnull=True)
def sort4(job):
        return job.order_by('-jobs_date_start').exclude(jobs_date_start__isnull=True)

# JOBS ZONE
def sort5(job):
        return job.order_by('jobs_zone')
def sort6(job):
        return job.order_by('-jobs_zone')

# JOBS TYPE (EXCLUDED FROM "PABEIGTIE DARBI")
def sort7(job):
        return job.order_by('jobs_type')
def sort8(job):
        return job.order_by('-jobs_type')


# JOBS DONE
def sort9(job):
    today = date.today()
    oldestDate = job.order_by('jobs_date_done')[0].jobs_date_done
    listEnd = True

    jobs = []
    d = 0 # day counter
    while (listEnd):
        try:
            dj = job.filter(jobs_date_done__startswith=( today - timedelta( days=d )))
            if dj.count() != 0:
                jobs.append(dj)
        except: # if day is empty
            pass
        if today - timedelta( days=d ) == oldestDate:
            listEnd = False
        d += 1 # increase day counter
    return jobs


def sort10(job):
    today = date.today()
    oldestDate = job.order_by('jobs_date_done')[0].jobs_date_done
    listEnd = True

    jobs = []
    d = 0 # day counter
    while (listEnd):
        try:
            dj = job.filter(jobs_date_done__startswith=( oldestDate + timedelta( days=d )))
            if dj.count() != 0:
                jobs.append(dj)
        except: # if day is empty
            pass
        if oldestDate + timedelta( days=d ) == today:
            listEnd = False
        d += 1 # increase day counter
    return jobs

sort_options = {1 : sort1, 2 : sort2, 3 : sort3, 4 : sort4, 5 : sort5, 6 : sort6, 7 : sort7, 8 : sort8, 9 : sort9, 10 : sort10,}
