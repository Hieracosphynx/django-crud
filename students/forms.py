from django import forms
from . import models
class NewStudentForm(forms.Form):

    CHOICES = models.Student().course_in_list()

    student_number = forms.CharField(label='student_number', max_length=20)
    first_name = forms.CharField(label='first_name', max_length=120)
    last_name = forms.CharField(label='last_name', max_length=120)
    course = forms.CharField(label='Course', widget=forms.Select(choices=models.Student().COURSE_IN_SCHOOL))