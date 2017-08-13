# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime
from django.contrib import messages
from django.utils.crypto import get_random_string
# the index function is called when root is visited
# def index(request):
# 	response = "Hello, This is your time page"
# 	return HttpResponse(response)

# def yourMethodFromUrls(request):
#   context = {
#   "somekey":"somevalue"
#   }
#   return render(request,'appname/page.html', context)

def index(request):
  context = {
  "time": strftime("%Y-%m-%d %I:%M %p %z", gmtime())
  }
  return render(request,'clock/index.html', context)
