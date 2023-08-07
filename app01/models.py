from django.db import models

# Create your models here.

class chimed(models.Model):
    # 中医药表
    cdescribe = models.CharField(max_length=1023)
    centity1 = models.CharField(max_length=255)
    crelationship = models.CharField(max_length=64)
    centity2 = models.CharField(max_length=255)
