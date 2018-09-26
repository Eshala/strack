from django.urls import path
from group import views

app_name = 'group'

urlpatterns = [
   path('create/',views.CreateGroup.as_view(), name='group_create'),
]