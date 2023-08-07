from django.db import models

class tibmed(models.Model):
    # 藏医药表
    describe = models.CharField(max_length=1023)
    entity1 = models.CharField(max_length=255)
    relationship = models.CharField(max_length=64)
    entity2 = models.CharField(max_length=255)
