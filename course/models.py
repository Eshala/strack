from django.db import models

# Create your models here.


class Course(models.Model):
    title = models.CharField(max_length=120)
    duration = models.IntegerField(default=0)
    price = models.IntegerField(default=0, blank=False)
    syllabus = models.TextField(blank=True)

    def __str__(self):
        return self.title