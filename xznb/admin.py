from django.contrib import admin
from .models import *

def turn_to_used(self,request,queryset):
    queryset.update(used = True)

class discountAdmin(admin.ModelAdmin):
    list_display = ('number','openid','alive','used','discount_class','creat_time')
    list_filter = ('alive',)
    search_fields = ('number',)
    actions = [turn_to_used]
    
admin.site.register(discount,discountAdmin)