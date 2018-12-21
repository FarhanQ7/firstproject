# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Topics(models.Model):

    topic = models.CharField(max_length=264, unique =True)

    def __str__(self):
        return self.topic


class Webpage(models.Model):

    category = models.ForeignKey(Topics)

    name = models.CharField(max_length=264)

    url = models.URLField()

    def __str__(self):
        return str(self.url)
