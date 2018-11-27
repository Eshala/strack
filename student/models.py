from django.conf import settings
from django.db import models
from course.models import Course
from group.models import Group, Shift
from datetime import datetime
from django import forms

class Student(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    address = models.CharField(max_length=120)
    phone_number = models.IntegerField(null=True)
    fee_submitted = models.IntegerField(default=0)
    course = models.ForeignKey(Course, null=True, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, null=True, on_delete=models.CASCADE)
    shift = models.ForeignKey(Shift, null=True, on_delete=models.CASCADE)
    photo = models.FileField(upload_to='bea', blank=True)
    marks = models.DecimalField(max_digits=3, decimal_places=2, default=0, blank=True)
    joined_date = models.DateField(blank=False, default= datetime.now())
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class Teacher(models.Model):
    name = models.CharField(max_length=120)
    address = models.CharField(max_length=120)
    phone_number = models.IntegerField(null=True)
    course = models.ForeignKey(Course, null=True, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, null=True, on_delete=models.CASCADE)
    shift = models.ForeignKey(Shift, null=True, on_delete=models.CASCADE)
    photo = models.FileField(upload_to='bea', blank=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.name

class Pay(models.Model):
    type = (("T", "Teacher"), ("S", "Student"), ("O", "Other"),)

    pay_to = models.CharField(max_length=200, blank=False)
    amount = models.DecimalField(decimal_places=2, default=0, blank=False, max_digits=5)
    paid_date = models.DateTimeField(blank=False, default=datetime.now())
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.CASCADE)
    type = models.CharField(choices=type, max_length=50, default="O", blank=False)
    by_cheque = models.BooleanField(default=False)
    cheque_no = models.DecimalField(decimal_places=0, blank=True, max_digits=5)
    courses = models.CharField(max_length=100, blank=True, null=True, editable=False)
    group = models.CharField(max_length=100, blank=True, null=True, editable=False)
    shift = models.CharField(max_length=100, blank=True, null=True, editable=False)
    remarks = models.TextField(blank=True)

    class Meta:
        ordering = ['paid_date']


