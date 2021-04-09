# -*- coding: utf-8 -*-
from django.template.defaultfilters import truncatechars  # or truncatewords
from django.db import models

# Django useri
from django.contrib.auth.models import User

import datetime


# JOB ZONES
class JobsZones(models.Model):
    class Meta():
        db_table = "jobs_zones"
        verbose_name_plural = "Darbu zonas"

    order = models.IntegerField( null=True, blank=True  )
    title = models.CharField( max_length=20, default="" )
    special = models.BooleanField( default=False )

    def __str__(self):
        return str(self.title)

# JOB TYPES
class JobsTypes(models.Model):
    class Meta():
        db_table = "jobs_types"
        verbose_name_plural = "Darbu veidi"

    order = models.IntegerField( null=True, blank=True  )
    type = models.CharField( max_length=20, default="" )

    marking_days = models.IntegerField( null=True, blank=True  )

    color = models.CharField( max_length=10, default="#f5f5f5" )
    started_color = models.CharField( max_length=10, default="#f5f5f5" )

    def __str__(self):
        return str(self.type)

# JOBS
class Jobs(models.Model):
    class Meta():
        db_table = "jobs"
        verbose_name_plural = "Darbu saraksts"

    jobs_user = models.ForeignKey( User, blank=True, null=True, on_delete=models.CASCADE )

    jobs_date_added = models.DateField( default=datetime.datetime.now, verbose_name="Darbs pievienots" )
    jobs_date_done = models.DateField( null=True, blank=True )
    jobs_date_start = models.DateField( null=True, blank=True, verbose_name="Darbs uzsākts" )

    jobs_descr = models.TextField( blank=False, verbose_name="Darba uzdevums" )

    jobs_zone = models.ForeignKey( JobsZones, blank=False, default=1, on_delete=models.CASCADE )
    jobs_type = models.ForeignKey( JobsTypes, null=False, blank=False, default=2, on_delete=models.CASCADE )

    jobs_link = models.URLField( max_length=200, blank=True, null=True, verbose_name="Saite" )

    jobs_done = models.BooleanField( default=False )
    jobs_cancel = models.BooleanField( default=False )

    marked = models.BooleanField( default=False )
    marked_until = models.DateField( null=True, blank=True, verbose_name="Izcelts līdz" )
    marked_id = models.IntegerField( null=True, blank=True, verbose_name="Izcelts Nr.p.k." )

    @property
    def jobs_descr_short(self):
        return truncatechars(self.jobs_descr, 60)
    jobs_descr_short.fget.short_description = u'Darba uzdevums saīsināts'

    @property
    def jobs_link_short(self):
        return "" if self.jobs_link is None else truncatechars(self.jobs_link, 30)
    jobs_link_short.fget.short_description = u'Darba saite saīsināts'

    def __str__(self):
        return str(self.jobs_date_added)


# ===============================================================================================
# OBJECT
class JobObj(models.Model):
    class Meta():
        db_table = "jobs_objects"
        verbose_name_plural = "Lietu parametri"

    obj_added = models.DateField( default=datetime.datetime.now, verbose_name="Darbs pievienots" )
    obj_title = models.CharField( max_length=50, blank=False )
    obj_descr = models.TextField( blank=True )

    obj_actual = models.BooleanField( default=False )

    obj_zone = models.ForeignKey( JobsZones, null=False, blank=False, default=1, on_delete=models.CASCADE )

    obj_url = models.URLField( max_length=200, blank=True, null=True )
    obj_nr = models.IntegerField( null=True, blank=True )

    def __str__(self):
        if self.obj_title == "":
            return u''
        else:
            return self.obj_title + " : " + str(self.obj_added)

# OBJECT IMAGES
class JobObj_image(models.Model):
    class Meta():
        db_table = "jobs_objects_images"
        verbose_name_plural = "Lietu parametru attēli"

    job_obj = models.ForeignKey( JobObj, default=1, related_name='o_i', on_delete=models.CASCADE )
    obj_image_big = models.ImageField( blank = True, null=True, upload_to = "job_obj/big/" )
    obj_image_small = models.ImageField( blank = True, null=True, upload_to = "job_obj/" )

    def __str__(self):
        return self.job_obj.obj_title + " : " + str(self.job_obj.obj_added)

# OBJECT FILES
class JobObj_file(models.Model):
    class Meta():
        db_table = "jobs_objects_files"
        verbose_name_plural = "Lietu parametru faili"

    job_obj = models.ForeignKey( JobObj, default=1, related_name='o_f', on_delete=models.CASCADE )
    obj_file = models.FileField( blank = True, null=True, upload_to = "job_obj/file/" )

    def __str__(self):
        return self.job_obj.obj_title
