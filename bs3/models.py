from django.db import models

# Create your models here.
class discount(models.Model):
    number = models.CharField(max_length = 15)
    openid = models.CharField(max_length = 100,
                              blank = True,)
    alive = models.BooleanField()