import django_filters

from student.models import Student, Teacher, Pay, GroupCourse, Marks


class StudentFilter(django_filters.FilterSet):
    class Meta:
        model = Student
        fields = {
            'name': ['icontains', ],
            'phone_number': ['icontains'],
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

class ResultFilter(django_filters.FilterSet):
    class Meta:
        model = Marks
        fields = {
            'course_detail__person_name': ['icontains', ],
            'course_detail__course': ['icontains', ],
            'course_detail__group': ['icontains', ],
            'course_detail__shift': ['icontains', ],
            'test_type': ['icontains',]
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