import django_filters

from student.models import Student


class StudentFilter(django_filters.FilterSet):
    class Meta:
        model = Student
        fields = ['name', 'course', 'group', 'shift']
