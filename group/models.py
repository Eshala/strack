from django.db import models

# Create your models here.
import datetime

class Subject(models.Model):
    name = models.CharField(max_length = 100, blank=False)
    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class Group(models.Model):
    name = models.CharField(max_length=120)
    subject_name = models.ForeignKey(Subject, blank=True, null=True, on_delete = models.CASCADE)

    def __str__(self):
        return self.name


class Shift(models.Model):
    name = models.CharField(max_length=120)
    start_time = models.TimeField(default=datetime.datetime.strptime('00:00', '%H:%M').time())
    end_time = models.TimeField(default=datetime.datetime.strptime('00:00', '%H:%M').time())

    def __str__(self):
        return self.name

