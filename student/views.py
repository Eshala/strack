from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .models import Student
from django.views.generic.list import ListView
from django.utils import timezone

class AddStudent(LoginRequiredMixin, CreateView):
    login_url = '/admin/login/'
    model = Student
    fields = [
        'name',
        'address',
        'phone_number',
        'fee_submitted',
        'course',
        'group',
        'shift',
    ]
    template_name = 'students/student_add.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class StudentList(LoginRequiredMixin, ListView):
    login_url = '/accounts/login/'
    template_name = 'students/student_list.html'
    queryset = Student.objects.all()
    context_object_name = 'student'
    paginate_by = 20

