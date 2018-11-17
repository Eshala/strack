from django.conf import settings
from django.db import models
from course.models import Course
from group.models import Group, Shift


class Student(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    address = models.CharField(max_length=120)
    phone_number = models.IntegerField(null=True)
    fee_submitted = models.IntegerField(default=0)
    course = models.ForeignKey(Course, null=True, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, null=True, on_delete=models.CASCADE)
    shift = models.ForeignKey(Shift, null=True, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.name
