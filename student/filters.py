import django_filters

from student.models import Student, Teacher


class StudentFilter(django_filters.FilterSet):
    class Meta:
        model = Student
        fields = ['name', 'course', 'group', 'shift']


class TeacherFilter(django_filters.FilterSet):
    class Meta:
        model = Teacher
        fields = ['name', 'course', 'group', 'shift']