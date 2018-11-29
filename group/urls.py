from django.urls import path
from group import views

app_name = 'group'

urlpatterns = [
   path('group/',views.CreateGroup.as_view(), name='group_create'),
   path('shift/',views.CreateShift.as_view(), name='shift_create'),
   path('subject/',views.createSubject.as_view(), name='subject_create'),
]