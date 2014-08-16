# Create your views here.
# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.http import HttpResponseRedirect , HttpResponse
from django.contrib import messages
from pytz import utc

from .models import *

import random

def xznb(request):
    if request.method == "POST":
        if request.POST.get("action","") == 'start': #clicked the start button
            if 'discount' in request.COOKIES and len(discount.objects.filter(number=request.COOKIES['discount']))>0:
                discount_number = request.COOKIES['discount']
                messages.warning(request, '重复抽奖！')
                current_user = discount.objects.get(number = discount_number)
                if current_user.alive == False:
                    messages.warning(request, "您的优惠券"+str(discount_number)+"尚未激活，请分享本页面给朋友或朋友圈！")
                return render_to_response('xznb_failed.html',RequestContext(request,{'discount_number':str(discount_number),
                                                                                     'discount_class':str(current_user.discount_class),}))
            else:
                discount_number = creat_discount()
                ip_addr = getIP(request)
                seed_class = "23"
                discount_class = random.choice(seed_class)
                t = discount.objects.create(number = discount_number,
                                            openid = str(ip_addr),
                                            alive = False,
                                            used = False,
                                            discount_class = discount_class,
                                            creat_time = utc.localize(datetime.datetime.now()),
                                            )
                t.save()
                r = render_to_response("xznb_result.html",RequestContext(request,{'discount_number':str(discount_number),
                                                                                  'discount_class':str(discount_class)}))
                r.set_cookie('discount',str(discount_number))
                return r
        if request.POST.get("action","") == 'about':
            return render_to_response("xznb_about.html",RequestContext(request))
        if request.POST.get("action","") == 'goStore':
            return HttpResponseRedirect('/xznb_gostore')
        if request.POST.get("action","") == 'backhome':
            return render_to_response("xznb_start_page.html",RequestContext(request))
        if request.POST.get("action","") == 'checkDiscount':
            discount_number = request.POST.get("name",'')
            u = discount.objects.filter(number = discount_number)
            if len(u)>0:
                if u[0].alive :
                    alive = '已激活'
                else:
                    alive = '未激活'
                if u[0].used:
                    used = "已使用"
                else:
                    used = "未使用"
                if u[0].discount_class == "2":
                    havetodo = "购物满299元"
                else:
                    havetodo = "无限制"
                return render_to_response("check_discount.html",RequestContext(request,{'discount_number':u[0].number,
                                                                                   'alive': alive,
                                                                                   'used': used,
                                                                                   'havetodo':havetodo}))
            else:
                return render_to_response("check_discount.html",RequestContext(request,{'discount_number':"未查到",
                                                                                   'alive':"未查到",
                                                                                   'used':"未查到",
                                                                                   'havetodo':"未查到"}))
    else:
        return render_to_response("xznb_start_page.html",RequestContext(request))
    
def xznb_gostore(request):
    agent = request.META.get('HTTP_USER_AGENT','')
    if 'MicroMessenger' in agent:
        messages.error(request,"由于微信浏览器功能有限，请使用其他浏览器访问本店！")
        return render_to_response('xznb_mmfailed.html',RequestContext(request))
    else:
        #return HttpResponse(str(request.META.get('HTTP_USER_AGENT','')))
        return HttpResponseRedirect("http://shop65572760.taobao.com/?spm=a230r.7195193.1997079397.2.kUoJUY")
    
    
def creat_discount():
    seed = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    sa = []
    for i in range(12):
        sa.append(random.choice(seed))
        salt = ''.join(sa)
    return salt

def getIP(request):
    ip_addr = []
    ip_addr.append(request.META.get("HTTP_X_FORWARDED_FOR","no HTTP_X_FORWARDED_FOR"))
    ip_addr.append(request.META.get("REMOTE_ADDR","no REMOTE_ADDR"))
    ip_addr.append(request.META.get("HTTP_CLIENT_IP","no HTTP_CLIENT_IP"))
    return ip_addr
    

def discount_about(request):
    return render_to_response('discount_about.html',RequestContext(request))

def wxconfirm(request):
    if 'discount' in request.COOKIES:
        discount_number = request.COOKIES['discount']
    t = discount.objects.filter(number = discount_number).update(alive = True)
    messages.success(request, "转发成功，您的优惠券"+str(discount_number)+"激活成功！")
    return HttpResponseRedirect('/xznb')

def get_info(request):
    raise
    values = request.META.items()
    values.sort()
    html = []
    for k, v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
    return HttpResponse('<table>%s</table>' % '\n'.join(html))

    
    
    