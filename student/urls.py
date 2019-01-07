from django.urls import path

from student import views
from student.models import Pay

app_name = 'student'
urlpatterns = [
   path('add/', views.AddStudent.as_view(), name='add_student'),
   path('add/student', views.AddTeacher.as_view(), name='add_teacher'),
   path('list/', views.search_student, name='list_student'),
   path('list/teacher', views.search_teacher, name='list_teacher'),
   path('studentdetail/<int:pk>/', views.StudentDetail.as_view(), name='studentdetail'),
   path('teacherdetail/<int:pk>/', views.TeacherDetail.as_view(), name='teacherdetail'),
   path('update/<int:pk>', views.updateDetail.as_view(), name='update'),
   path('bill/', views.PayBill.as_view(), name='paybill'),
   path('bill/list/', views.bill_report, name='report'),
   path('updatepay/', views.updatePay, name='updatepay'),
   path('addcourseandgroup/', views.addCourseandShifts, name='addcoursegroup'),
   path('delete/', views.course_delete_view, name='deletecoursegroup'),
   path('updatemarks/', views.course_mark_update_view, name='updatecoursegroup'),
   path('marks/', views.exam_list, name='examlist'),
   path('billinfo/', views.getBillInfo, name='billinfo'),
   path('cancel/', views.cancelBill, name='cancelbill'),
   path('cancel/list', views.bill_report_cancelled, name='cancelbilllist'),
   path('archive/', views.archiveBill, name='archive'),
   path('marks/update/', views.updateMarks, name = 'updatemarks'),
   path('result/', views.studentResult, name='result')
   # path('subjectlist/', )
]