from django.urls import path
from student import views

app_name = 'student'

urlpatterns = [
   path('add/', views.AddStudent.as_view(), name='add_student'),
   path('add/student', views.AddTeacher.as_view(), name='add_teacher'),
   path('list/', views.search_student, name='list_student'),
   path('list/teacher', views.search_teacher, name='list_teacher'),
   path('studentdetail/<int:pk>/', views.StudentDetail.as_view(), name='studentdetail'),
   path('teacherdetail/<int:pk>/', views.TeacherDetail.as_view(), name='teacherdetail'),
]