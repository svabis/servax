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

#def rand_slug():
#    return str( uuid.uuid4() ).split("-")[4]

def upload_path(instance, filename):
#    return os.path.join('garden/', slugify(unicode(filename)) )
    return os.path.join('garden/', slugify(filename) )


# =================================================================================================================
class SuperTheme(models.Model):
    class Meta():
        db_table = "super_tema"

    order = models.IntegerField( default = 0 )
    title = models.CharField( max_length = 100 )
    slug = models.SlugField( unique = True, max_length=50 ) #, default=rand_slug(title) )

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(SuperTheme, self).save(*args, **kwargs)

# =================================================================================================================
class Theme(models.Model):
    class Meta():
        db_table = "tema"

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
        db_table = "ieraksts"

    relate_to = models.ForeignKey( Theme, default = 1, on_delete=models.CASCADE )

    user = models.ForeignKey( User, default = 1, on_delete=models.CASCADE )

    date = models.DateTimeField( default = timezone.now )
    text = models.TextField( max_length = 500 )

    image = models.ImageField( blank = True, null = True, upload_to = upload_path)

    @property
    def text_short(self):
        return truncatechars(self.text, 60)
    text_short.fget.short_description = u'text short'
