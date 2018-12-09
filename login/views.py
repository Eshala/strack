from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django_jinja.views.generic import ListView

from login.LoginDecorator import superuser_required
from . import register_user_form
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseForbidden

class SignUP(CreateView):
    form_class = register_user_form.UserCreateForm
    success_url = reverse_lazy('home')
    template_name = 'accounts/register_user.html'


class HomePage(LoginRequiredMixin, TemplateView):
    template_name = 'index.html'


class ThanksPage(TemplateView):
    template_name = 'thanks.html'


@user_passes_test(lambda u: u.is_superuser)
def UserList(request):
    data = User.objects.all()
    print(len(data))
    return render(request, 'accounts/userlist.html', {'user': data})

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('change_password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'accounts/change_password.html', {
        'form': form
    })
