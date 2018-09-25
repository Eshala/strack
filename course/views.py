from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView

from course import course_form


class CreateCourse(CreateView):
    form_class = course_form.CourseForm
    success_url = reverse_lazy('course:course_create')
    template_name = 'courses/create_course.html'
