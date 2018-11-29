from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView

from group import form


class CreateGroup(CreateView):
    form_class = form.GroupForm
    success_url = reverse_lazy('group:group_create')
    template_name = 'groups/create_group.html'


class CreateShift(CreateView):
    form_class = form.ShiftForm
    success_url = reverse_lazy('group:shift_create')
    template_name = 'shift/create_shift.html'

class createSubject(CreateView):
    form_class = form.SubjectForm
    success_url = reverse_lazy('group:subject_create')
    template_name = 'subject/create_subject.html'
