from anaconda_project.internal.cli import archive
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
from django.forms import forms
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic import DetailView
from django.views.generic import UpdateView
from django.urls import reverse
from rest_framework.serializers import Serializer

from course.models import Course
from group.models import Group, Shift, Subject
from student.filters import StudentFilter, TeacherFilter, BillFilter, ExamFilter, ResultFilter
from .models import Student, Teacher, Pay, GroupCourse, Marks
from django.views.generic.list import ListView
from django.utils import timezone
import django_filters
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
import json
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Sum
import functools
from django.contrib import messages
from django.core import serializers

class AddStudent(LoginRequiredMixin, CreateView):
    login_url = '/admin/login/'
    model = Student
    fields = [
        'name',
        'address',
        'phone_number',
        'joined_date',
        'photo',
    ]
    template_name = 'students/student_add.html'
    success_url = reverse_lazy('home')

    # def get_form(self, form_class=None):
    #     if form_class is None:
    #         form_class = self.get_form_class()
    #     form_class.__dict__['base_fields']['joined_date'].widget = (forms.SelectDateWidget())
    #     return form_class(**self.get_form_kwargs())

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    pass

def course_delete_view(request):
    print("in delete request")
    if request.method == "POST" and request.user.is_authenticated:
        id = request.POST.get('id')
        cg = get_object_or_404(GroupCourse, id=id)
        cg.delete()
        messages.success(request, "Course group successfully deleted!")
        return HttpResponse(json.dumps({"status":True, "message": "deleted successfully"}))
    return HttpResponse(json.dumps({"status": False, "message": "deleted failed"}))

def course_mark_update_view(request):
    print("in update request")
    if request.method == "POST" and request.user.is_authenticated:
       id = request.POST.get('id')
       cg = get_object_or_404(GroupCourse, id=id)
       cg.marks = request.POST.get('marks')
       cg.save()
       messages.success(request, "marks successfully updated!")
       return HttpResponse(json.dumps({"status":True, "message": "marks successfully updated"}))
            # return HttpResponse(json.dumps({"status": False, "message": "marks update failed"}))

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

class updateDetail(LoginRequiredMixin, UpdateView):
    login_url = '/admin/login/'
    model = Student
    success_url = reverse_lazy('home')
    pk_url_kwarg = 'pk'
    fields = [
        'name',
        'address',
        'phone_number',
        'joined_date',
        'photo',
    ]
    template_name = 'students/student_add.html'
    def form_valid(self, form):
        post = form.save(commit=False)
        post.save()
        return redirect('../studentdetail/'+str(self.object.pk))


def calculateTotal(fees):
    total = 0
    for fee in fees:
        total += fee.amount
    return total
    pass


class StudentDetail(LoginRequiredMixin, DetailView):
    login_url = '/admin/login/'
    template_name = 'students/studentdetail.html'
    success_url = reverse_lazy('home')
    model = Student

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(self.kwargs['pk'])
        data = Student.objects.get(id= self.kwargs['pk']);
        context['student'] = data
        fees = Pay.objects.filter(payto_id= self.kwargs['pk'], type__contains='STU')
        context['total'] = calculateTotal(fees)
        context['fees'] = fees
        context['group'] = Group.objects.all()
        context['shift'] = Shift.objects.values_list('name', flat=True)
        context['course'] = Course.objects.all()
        context['coursegroup'] = GroupCourse.objects.filter(person_type__contains='STU', person_id=self.kwargs['pk'])
        return context
    pass


class TeacherDetail(LoginRequiredMixin, DetailView):
    login_url = '/admin/login/'
    template_name = 'students/studentdetail.html'
    success_url = reverse_lazy('home')
    model = Teacher

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(self.kwargs['pk'])
        context['student'] = Teacher.objects.get(id= self.kwargs['pk'])
        fees = Pay.objects.filter(type__contains='TEA', payto_id=self.kwargs['pk'])
        context['fees'] = fees
        context['total'] = calculateTotal(fees)
        context['isTeacher'] = True
        context['group'] = Group.objects.all()
        context['shift'] = Shift.objects.values_list('name', flat=True)
        context['course'] = Course.objects.all()
        context['subject'] = Subject.objects.all()
        context['coursegroup'] = GroupCourse.objects.filter(person_type__contains='TEA', person_id=self.kwargs['pk'])
        print(context)
        return context
    pass

class PayBill(LoginRequiredMixin, CreateView):
    login_url = '/admin/login/'
    success_url = reverse_lazy('home')
    fields = ['pay_to', 'amount', 'by_cheque', 'cheque_no', 'type', 'remarks', 'transaction_type', 'paid_date']
    template_name = 'students/billpay.html'
    model = Pay
    def form_valid(self, form):
        pay = form.save(commit=False)
        pay.user = self.request.user
        pay.save()
        return super().form_valid(form)


class AddTeacher(LoginRequiredMixin, CreateView):
    login_url = '/admin/login/'
    model = Teacher
    fields = [
        'name',
        'address',
        'phone_number',
        'photo',
    ]
    template_name = 'students/teacher_add.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

def updatePay(request):
    if request.method == 'POST':
        try:
            pay_to = request.POST.get('pay_to')
            amount = request.POST.get('amount')
            type = request.POST.get('type')
            group = request.POST.get('group')
            course = request.POST.get('course')
            shift = request.POST.get('shift')
            subject = request.POST.get('subject')
            hour = request.POST.get('hour')
            if not subject:
                subject = ''
            if not hour:
                hour = 0
            remarks = request.POST.get('remarks')
            payto_id = request.POST.get('payto_id')
            transaction_type = request.POST.get('transaction_type')
            print(request.POST)
            pay = Pay(pay_to=pay_to, amount=amount, type=type, user=request.user, group=group, courses=course, shift = shift, subject=subject, hours = int(hour), paid_date=timezone.now(), remarks=remarks, payto_id=payto_id, transaction_type=transaction_type)
            pay.save()
            return HttpResponse(json.dumps({'status': True, 'message': str(amount)+ " paid successfully"}))
        except :
            return HttpResponse(json.dumps({'status': False, 'message': 'Problems in adding the amount'}))

def search_student(request):
    student_list = Student.objects.all()
    student_filter = StudentFilter(request.GET, queryset=student_list)
    return render(request, 'students/student_list.html', {'filter': student_filter, 'isTeacher': False})

def search_teacher(request):
    teacher_list = Teacher.objects.all()
    teacher_filter = TeacherFilter(request.GET, queryset=teacher_list)
    return render(request, 'students/student_list.html', {'filter': teacher_filter, 'isTeacher': True})


def getIncomeExpense(bill_list):
    income_expense = {'total':0,
                      'expense':0,
                      'remain':0}
    income = 0
    expense = 0
    for bill in bill_list :
        if bill.transaction_type == 'C':
            expense += int(bill.amount)
        else:
            income += int(bill.amount)
    total = income + expense
    income_expense['expense'] = expense
    income_expense['total'] = total
    income_expense['remain'] = income
    return income_expense
    pass

def updateMarks(request):
    if request.method == 'POST':
        postData = request.POST.get('marks_data')
        marksData = json.loads(postData)
        for m in marksData:
            print(m)
            myMark = Marks(course_detail_id = m['id'], marks = m['marks'], test_type = m['exa_type'])
            myMark.save()
        return HttpResponse(json.dumps({'success': True, 'message': 'Marks updates successfully'}))
    return HttpResponse(json.dumps({'success': False, 'message': 'Marks updates failed'}))

def cancelBill(request):
    return render(request, 'students/cancelpayment.html')

def archiveBill(request):
    try:
        id = request.GET.get('id')
        bill = Pay.objects.get(pk=id)
        bill.archive= True
        bill.save()
        return HttpResponse(json.dumps({'success': True, 'message': "Bill is cancelled successfully"}))

    except Pay.DoesNotExist:
        return HttpResponse(json.dumps({'success': False, 'message': 'Error in cancelling bill'}))

def getBillInfo(request):
    try:
        id = request.GET.get('id')
        bill = Pay.objects.get(pk=id)
        return HttpResponse(json.dumps({'success': True, 'data': json.dumps(bill.toJSON())}))

    except Pay.DoesNotExist:
        return HttpResponse(json.dumps({'success': False, 'message': 'Could not found the following bill'}))

def exam_list(request):
    ex_list = GroupCourse.objects.filter(person_type__contains='STU')
    exam_filter = ExamFilter(request.GET, queryset=ex_list)
    return render(request, 'students/markentry.html', {'filter': exam_filter})

def bill_report(request):
    if request.user.is_superuser:
        bill_list = Pay.objects.filter(archive=False)
    else:
        bill_list = Pay.objects.filter(user=request.user)
    bill_filter = BillFilter(request.GET, queryset=bill_list)
    income_expense = getIncomeExpense(bill_list)
    return render(request, 'students/billreport.html', {'filter': bill_filter, 'expense':income_expense['expense'], 'total': income_expense['total'], 'remain': income_expense['remain']})

def bill_report_cancelled(request):
    if request.user.is_superuser:
        bill_list = Pay.objects.filter(archive=True)
    else:
        bill_list = Pay.objects.filter(user=request.user)
    bill_filter = BillFilter(request.GET, queryset=bill_list)
    income_expense = getIncomeExpense(bill_list)
    return render(request, 'students/billreport.html', {'filter': bill_filter, 'total': income_expense['total']})

def studentResult(request):
    ex_list = Marks.objects.all()
    result_filter = ResultFilter(request.GET, queryset=ex_list)
    return render(request, 'students/student_result.html', {'filter': result_filter})

def addCourseandShifts(request):
    try:
        course = request.POST.get('course')
        group = request.POST.get('group')
        shift = request.POST.get('shift')
        user_type = request.POST.get('type')
        user_id = request.POST.get('uid')
        name = request.POST.get('name')
        discount = request.POST.get('discount')
        amount = request.POST.get('amount')
        subjects = ''
        if 'subjects' in request.POST.keys() and request.POST['subjects']:
            subjects = request.POST.get('subjects')

        print("{}, {}, {},{}".format(course, group, shift, user_id))
        courseshift = GroupCourse(course=course, group=group, shift=shift, person_type=user_type, person_id = user_id, amount=int(amount), discount=int(discount), person_name=name, subject= subjects)
        courseshift.save()
        return HttpResponse(json.dumps({'status': True, 'message': 'Added successfully in the database'}))
    except:
        print("cannot saved")
        return HttpResponse(json.dumps({'status': False, 'message': 'Cannot add the course, Please try again'}))
    pass