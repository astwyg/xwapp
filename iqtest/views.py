# Create your views here.
# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.contrib import messages
import random

from .forms import *


def start_page(request):
    if request.method=="POST":
        print request.POST.get('action','')
        if request.POST.get('action','')=='start':
            question_number = 1
            messages.success(request,"第"+str(question_number)+"题，共9题")
            return render_to_response('question.html',RequestContext(request,{'form':question_1,
                                                                              'theString':Q1,
                                                                              'question_number':question_number,}))
        elif request.POST.get('action','')=='1':
            question_number = 2
            messages.success(request,"第"+str(question_number)+"题，共9题")
            return render_to_response('question.html',RequestContext(request,{'form':question_2,
                                                                              'theString':Q2,
                                                                              'question_number':question_number,}))
        elif request.POST.get('action','')=='2':
            question_number = 3
            messages.success(request,"第"+str(question_number)+"题，共9题")
            return render_to_response('question.html',RequestContext(request,{'form':question_3,
                                                                              'theString':Q3,
                                                                              'question_number':question_number,}))
        elif request.POST.get('action','')=='3':
            question_number = 4
            messages.success(request,"第"+str(question_number)+"题，共9题")
            return render_to_response('question.html',RequestContext(request,{'form':question_4,
                                                                              'theString':Q4,
                                                                              'question_number':question_number,
                                                                              }))
        elif request.POST.get('action','')=='4':
            question_number = 5
            messages.success(request,"第"+str(question_number)+"题，共9题")
            return render_to_response('question.html',RequestContext(request,{'form':question_5,
                                                                              'theString':Q5,
                                                                              'question_number':question_number,
                                                                              'showAD':True,}))
        elif request.POST.get('action','')=='5':
            question_number = 6
            messages.success(request,"第"+str(question_number)+"题，共9题")
            return render_to_response('question.html',RequestContext(request,{'form':question_6,
                                                                              'theString':Q6,
                                                                              'question_number':question_number,
                                                                              'showAD':True,}))
        elif request.POST.get('action','')=='6':
            question_number = 7
            messages.success(request,"第"+str(question_number)+"题，共9题")
            return render_to_response('question.html',RequestContext(request,{'form':question_7,
                                                                              'theString':Q7,
                                                                              'question_number':question_number,
                                                                              'showAD':True,}))
        elif request.POST.get('action','')=='7':
            question_number = 8
            messages.success(request,"第"+str(question_number)+"题，共9题")
            return render_to_response('question.html',RequestContext(request,{'form':question_8,
                                                                              'theString':Q8,
                                                                              'question_number':question_number,
                                                                              'showAD':True,}))
        elif request.POST.get('action','')=='8':
            question_number = 9
            messages.success(request,"第"+str(question_number)+"题，共9题")
            return render_to_response('question.html',RequestContext(request,{'form':question_9,
                                                                              'theString':Q9,
                                                                              'question_number':question_number,
                                                                              'showAD':True,}))
        elif request.POST.get('action','')=='9':
            messages.success(request,"恭喜！测试结束，请点击右上角分享到朋友圈查看结果！")
            score=str(120+(random.randint(0,400)-200)/20.0)
            return render_to_response('result.html',RequestContext(request,{'form':question_9,
                                                                              'score':score,
                                                                              }))
            
    else:    
        messages.warning(request,"本测试共9题，大约需要15分钟！")
        return render_to_response('start_page.html',RequestContext(request))