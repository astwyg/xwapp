#coding=utf-8
from django.db import models
import datetime

class Info(models.Model):
    title = models.CharField("标题",max_length=20)
    creat_time = models.DateTimeField("添加时间",default=datetime.datetime.now(), blank=True, null=True)
    tags = models.CharField("标签集",max_length=20)
    content = models.TextField("内容",max_length = 5000)
    class Meta:
        verbose_name = '信息'
        verbose_name_plural = '信息'
        ordering = ['-creat_time']
    def __unicode__(self):
        return self.title
