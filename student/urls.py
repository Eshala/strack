from django.urls import path
from student import views

app_name = 'student'

urlpatterns = [
   path('add/', views.AddStudent.as_view(), name='add_student'),
]