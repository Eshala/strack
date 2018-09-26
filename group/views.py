from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView

from group import group_form


class CreateGroup(CreateView):
    form_class = group_form.GroupForm
    success_url = reverse_lazy('group:group_create')
    template_name = 'groups/create_group.html'