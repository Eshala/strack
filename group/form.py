from datetimepicker.widgets import DateTimePicker
from django import forms
from .models import Group, Shift, Subject


class GroupForm(forms.ModelForm):
    subject_name = forms.ModelMultipleChoiceField(
        queryset= Subject.objects.all(),
        widget=forms.CheckboxSelectMultiple)
    class Meta:
        model = Group
        fields = [
            'name',
            'subject_name',
        ]

class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = [
            'name'
        ]

class ShiftForm(forms.ModelForm):
    # valid_time_formats = ['%P', '%H:%M%A', '%H:%M %A', '%H:%M%a', '%H:%M %a']
    # start_time = forms.TimeField(
    #     widget=DateTimePicker(options={
    #         "pickTime": True,
    #         "pickDate": False,
    #         "minuteStepping": 1,
    #         "sideBySide": True,
    #     }),
    #     input_formats=valid_time_formats
    # )
    class Meta:
        model = Shift
        fields = [
            'name',
            'start_time',
            'end_time'
        ]
