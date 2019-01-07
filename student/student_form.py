from django import forms
from .models import Student, StudentEnquiry


# class StudentForm(forms.ModelForm):
#     class Meta:
#         model = Student
#         fields = [
#             'name',
#             'address',
#             'phone_number',
#             'fee_submitted',
#             'course',
#             'group',
#             'shift',
#         ]



class EnquiryStudentForm(forms.ModelForm):
    class Meta:
        model = StudentEnquiry
        fields = [
            'name',
            'address',
            'phone_number',
            'intrested_join_date',
            'enquiry_date',
            'intrested_course'
        ]
