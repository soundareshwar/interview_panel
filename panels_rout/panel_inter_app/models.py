from django.db import models

# Create your models here.

class Panel_Inter(models.Model):
    name = models.CharField(max_length=30)
    skills = models.CharField(max_length=30)
    outstation = models.BooleanField(default=False)
    weekend = models.BooleanField(default=False)

class Schedule_Inter(models.Model):
    name = models.CharField(max_length=30)
    date = models.CharField(max_length=10)
#    change_history = models.CharField(max_length=20)
