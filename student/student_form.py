from django import forms
from .models import Student


class StudentForm(forms.ModelForm):
    class Meta:
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
