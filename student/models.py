from django.conf import settings
from django.db import models

# Create your models here.
from course.models import Course
from group.models import Group, Shift


class Student(models.Model):
    name = models.CharField(max_length=120)
    address = models.CharField(max_length=120)
    phone_number = models.IntegerField(blank=True)
    fee_submitted = models.IntegerField(default=0)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    shift = models.ForeignKey(Shift, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.name


