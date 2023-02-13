from __future__ import unicode_literals
from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.urls import reverse


class Reg(models.Model):
    user = models.CharField(primary_key=True,max_length=20)
    pwd = models.CharField(max_length=20)
    fname=models.CharField(max_length=10)
    lname=models.CharField(max_length=20)
    dob=models.DateField()
    mobno=models.IntegerField()
    
