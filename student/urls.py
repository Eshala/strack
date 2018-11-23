from django.urls import path
from student import views

app_name = 'student'

urlpatterns = [
   path('add/', views.AddStudent.as_view(), name='add_student'),
   path('list/', views.StudentList.as_view(), name='list_student'),
   path('test/', views.search, name='test'),
]