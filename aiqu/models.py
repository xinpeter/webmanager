from django.db import models
import time
# Create your models here.
class Test(models.Model):
    name = models.CharField(max_length=20)
    password = models.CharField(max_length=30)
    date = models.CharField(max_length=61)

