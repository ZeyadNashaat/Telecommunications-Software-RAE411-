# -*- coding: utf-8 -*-
"""
Created on Wed May 24 01:30:21 2023

@author: Zeyad Mohamed
"""

from django.urls import path
from . import views
urlpatterns = [
   path('', views.HTML),]