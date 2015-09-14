# -*- coding:utf-8 -*-

from django.http import HttpResponseRedirect, HttpResponse
from django.template.context import RequestContext
from django.shortcuts import render_to_response as render
import sae.kvdb, sys

kv = sae.kvdb.Client()

def index(request):
    reload(sys) 
    sys.setdefaultencoding('utf8')
    
    #testing
    tag = "测试"
    contents = kv.get_by_prefix(tag)
    return render('index/index.htm',RequestContext(request,locals()))