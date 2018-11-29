import django_filters

from student.models import Student, Teacher, Pay


class StudentFilter(django_filters.FilterSet):
    class Meta:
        model = Student
        fields = {
            'name': ['icontains', ],
            'course': ['exact', ],
            'group':['exact', ],
            'shift':['exact', ]
        }


class TeacherFilter(django_filters.FilterSet):
    class Meta:
        model = Teacher
        fields = {
            'name': ['icontains', ],
            'course': ['exact', ],
            'group': ['exact', ],
            'shift': ['exact', ]
        }

class BillFilter(django_filters.FilterSet):
    class Meta:
        model = Pay
        fields = {
            'type': ['exact', ],
            'paid_date': ['gt','lt'],
        }