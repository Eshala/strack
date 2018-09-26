from django.urls import path
from course import views

app_name = 'course'

urlpatterns = [
   path('create/',views.CreateCourse.as_view(), name='course_create'),
]