from django.db import models

# Create your models here.
import datetime


class Group(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name


class Shift(models.Model):
    name = models.CharField(max_length=120)
    start_time = models.TimeField(default=datetime.datetime.strptime('00:00', '%H:%M').time())
    end_time = models.TimeField(default=datetime.datetime.strptime('00:00', '%H:%M').time())

    def __str__(self):
        return self.name