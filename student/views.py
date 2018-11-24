from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from course.models import Course
from group.models import Group
from student.filters import StudentFilter, TeacherFilter
from .models import Student, Teacher
from django.views.generic.list import ListView
from django.utils import timezone
import django_filters

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
    pass

# class StudentList(LoginRequiredMixin, ListView):
#     login_url = '/accounts/login/'
#     template_name = 'students/student_list.html'
#     queryset = Student.objects.all()
#     context_object_name = 'student'
#
#     def get_context_data(self, **kwargs):
#         context = super(StudentList, self).get_context_data(**kwargs)
#         context['course'] = Course.objects.all()
#         context['group'] = Group.objects.all()
#         # And so on for more models
#         return context

class AddTeacher(LoginRequiredMixin, CreateView):
    login_url = '/admin/login/'
    model = Teacher
    fields = [
        'name',
        'address',
        'phone_number',
        'course',
        'group',
        'shift',
    ]
    template_name = 'students/teacher_add.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

def search_student(request):
    student_list = Student.objects.all()
    student_filter = StudentFilter(request.GET, queryset=student_list)
    return render(request, 'students/student_list.html', {'filter': student_filter, 'isTeacher': False})

def search_teacher(request):
    teacher_list = Teacher.objects.all()
    teacher_filter = TeacherFilter(request.GET, queryset=teacher_list)
    return render(request, 'students/student_list.html', {'filter': teacher_filter, 'isTeacher': True})