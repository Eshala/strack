import django_filters

from student.models import Student, Teacher, Pay, GroupCourse


class StudentFilter(django_filters.FilterSet):
    class Meta:
        model = Student
        fields = {
            'name': ['icontains', ]
        }


class TeacherFilter(django_filters.FilterSet):
    class Meta:
        model = Teacher
        fields = {
            'name': ['icontains', ],
        }

class BillFilter(django_filters.FilterSet):
    class Meta:
        model = Pay
        fields = {
            'type': ['exact', ],
            'transaction_type':['exact',],
            'paid_date': ['gt','lt'],
            'user': ['exact']
        }

class ExamFilter(django_filters.FilterSet):
    class Meta:
        model = GroupCourse
        fields = {
            'person_name': ['icontains', ],
            'course': ['icontains', ],
            'group': ['icontains', ],
            'shift': ['icontains', ],

        }