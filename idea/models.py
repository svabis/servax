# -*- coding: utf-8 -*-
from django.template.defaultfilters import truncatechars  # or truncatewords
from django.utils import timezone
from django.db import models

from django.contrib.auth.models import User # autorisation library

import os
#from datetime import datetime

import uuid
import random
import string

#from unidecode import unidecode
from slugify import slugify

def upload_path(instance, filename):
    return os.path.join('garden/', slugify(filename) )

def upload_new_path(instance, filename):
    return os.path.join('idea/', slugify(filename) )



# =================================================================================================================
class SuperTheme(models.Model):
    class Meta():
        db_table = "idea_super_tema"
        verbose_name_plural = "Ideju Lāde - tabi"

    order = models.IntegerField( default = 0 )
    title = models.CharField( max_length = 100 )
    slug = models.SlugField( unique = True, max_length=50 )

    icon = models.CharField( max_length = 100, default='', blank = True, null = True )

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(SuperTheme, self).save(*args, **kwargs)

# =================================================================================================================
class Theme(models.Model):
    class Meta():
        db_table = "idea_tema"
        verbose_name_plural = "Ideju Lāde - tēmas"

    relate_to_super = models.ForeignKey( SuperTheme, default=1, on_delete=models.CASCADE )
    parent = models.ForeignKey( 'Theme', blank=True, null=True, on_delete=models.CASCADE )

    created_by = models.ForeignKey( User, default = 1, on_delete=models.CASCADE )
    created_date = models.DateTimeField( default = timezone.now )

    title = models.CharField( max_length = 100 )
    slug = models.SlugField( unique = True, max_length=50 ) #, default=rand_slug() )
    last_entry = models.DateTimeField( default = timezone.now )
    entry_count = models.IntegerField( default = 0 )

    comment = models.BooleanField( default=False ) # coments enabled

    def __str__(self):
        return self.title


# =================================================================================================================
class Post(models.Model):
    class Meta():
        db_table = "idea_ieraksts"
        verbose_name_plural = "Ideju Lāde - ieraksti"

    relate_to = models.ForeignKey( Theme, default = 1, on_delete=models.CASCADE )

    user = models.ForeignKey( User, default = 1, on_delete=models.CASCADE )

    date = models.DateTimeField( default = timezone.now )
    text = models.TextField( max_length = 500, blank=True, null=True )

#    image = models.ImageField( blank = True, null = True, upload_to = upload_path)
    url = models.URLField( max_length=200, blank=True, null=True )

    @property
    def text_short(self):
        return truncatechars(self.text, 60)
    text_short.fget.short_description = u'text short'

    def __str__(self):
        name = str(self.date)[:10] + "  "
        if self.text != "":
            name += self.text[:20].replace("\n","")
        return name

# =================================================================================================================
class PostImage(models.Model):
    class Meta():
        db_table = "idea_images"
        verbose_name_plural = "Ideju Lāde - attēli"

    post = models.ForeignKey( Post, default = 1, on_delete=models.CASCADE, related_name='img' )
    image = models.ImageField( blank = True, null = True, upload_to = upload_new_path)
