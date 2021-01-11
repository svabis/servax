# -*- coding: utf-8 -*-
from django.db import models

from django.utils import timezone


# !!!!! BILDE !!!!!
class Galery(models.Model):
    class Meta():
        db_table = "gallery"

    galery_date = models.DateField( default = timezone.now )

    galery_img = models.ImageField( upload_to = "galery/" )
    galery_thumb = models.ImageField( upload_to = "galery/thumb/", blank=True, null=True )

    galery_public = models.BooleanField( default = False )

    galery_tags = models.CharField( max_length=100, blank=True )

    def __str__(self):
        return str(self.galery_date)
