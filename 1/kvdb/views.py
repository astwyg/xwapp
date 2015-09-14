# -*- coding:utf-8 -*-
from django.http import HttpResponseRedirect, HttpResponse
import sae.kvdb, sys
from django.views.decorators.csrf import csrf_exempt

kv = sae.kvdb.Client()

@csrf_exempt
def api(request):
    reload(sys) 
    sys.setdefaultencoding('utf8')
    
    func = request.POST.get("func")
    if(func == "set"):
        key = str(request.POST.get("key"))
        value = request.POST.get("value")
        r = kv.set(key,value)
    elif(func == "get"):
        prefix = str(request.POST.get("prefix"))
        pair = kv.get_by_prefix(prefix)
        r = ""
        for ins in pair:
            r = "/r/n" + ins[0] + "|" + ins[1]
    else:
        r="invalid function name"
    return HttpResponse(str(r))