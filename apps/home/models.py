# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class EventList(models.Model):
    username = models.ForeignKey(User, on_delete = models.CASCADE)
    eventname = models.CharField(max_length=50)
    eventdate = models.DateField(null=True)
    predtime = models.FloatField(max_length=50)
    emerge = models.CharField(max_length=50)
    iscomplete = models.BooleanField(default=False)
    costtime = models.FloatField(null=True, blank=True)

    class Meta:
      ordering: ['eventdate']      


    def __str__(self):
        return 'user: %s eventname: %s %s %s %s %s %s'%(self.username, self.eventname, self.eventdate, self.predtime, self.emerge, self.iscomplete , self.costtime)


class Dailyfreetime(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    timedate = models.DateField(null=True)
    freetime = models.FloatField(max_length=50)
    busytime = models.FloatField(max_length=50, null=True)

    def __str__(self):
        return '%s %s %s %s'%(self.username, self.timedate, self.freetime, self.busytime)
