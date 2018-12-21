# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render


def index(requests):

    my_dict = {'insert_me':"Asalamualykum"}

    return render(requests,'index.html',context = my_dict)

# Create your views here.
