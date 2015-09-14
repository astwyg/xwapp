#coding=utf-8
from django.contrib import admin
from .models import *
from django import forms
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.shortcuts import render_to_response
from django.template.context import RequestContext
import datetime

class InfoAdmin(admin.ModelAdmin):
    verbose_name = '信息管理'
    verbose_name_plural = '信息管理'
    list_display = ('title','tags',"creat_time","content")
    
admin.site.register(Info, InfoAdmin)



            
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    