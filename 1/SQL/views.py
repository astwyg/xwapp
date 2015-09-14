# -*- coding:utf-8 -*-
from django.http import HttpResponseRedirect, HttpResponse
import sae.kvdb, sys, datetime
from django.views.decorators.csrf import csrf_exempt
from .models import Info

@csrf_exempt
def api(request):
    reload(sys) 
    sys.setdefaultencoding('utf8')
    
    func = request.POST.get("func")
    if(func == "set"):
        title = request.POST.get("title")
        content = request.POST.get("content")
        tags = request.POST.get("tags")
        creat_time = datetime.datetime.now()
        t = Info(title = title,
                 content = content,
                 tags = tags,
                 creat_time = creat_time)
        t.save()
        r = t.id
    elif(func == "get"):
        prefix = str(request.POST.get("id"))
        info = Info.objects.get(id = id)
        r = info.title+info.content
    else:
        r="invalid function name"
    return HttpResponse(str(r))