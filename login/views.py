from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from . import register_user_form


class SignUP(CreateView):
    form_class = register_user_form.UserCreateForm
    success_url = reverse_lazy('home')
    template_name = 'accounts/register_user.html'


class HomePage(LoginRequiredMixin, TemplateView):
    template_name = 'index.html'


class ThanksPage(TemplateView):
    template_name = 'thanks.html'

