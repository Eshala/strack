from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView

from . import student_form


class AddStudent(CreateView):
    form_class = student_form.StudentForm
    success_url = reverse_lazy('student:add_student')
    template_name = 'students/student_add.html'