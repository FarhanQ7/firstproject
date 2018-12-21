# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from first_app.models import Topics , Webpage
#Register your models here.

admin.site.register(Topics)
admin.site.register(Webpage)
