from django.db import models
import datetime

# Create your models here.
class discount(models.Model):
    number = models.CharField(max_length = 15)
    openid = models.CharField(max_length = 100,
                              blank = True,)
    alive = models.BooleanField()
    used = models.BooleanField()
    discount_class = models.CharField(max_length = 2)
    creat_time = models.DateTimeField(default=datetime.datetime.now())