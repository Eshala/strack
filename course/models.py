from django.db import models

# Create your models here.


class Course(models.Model):
    title = models.CharField(max_length=120)
    duration = models.IntegerField(default=0)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    syllabus = models.TextField(blank=True)

    def __str__(self):
        return self.title