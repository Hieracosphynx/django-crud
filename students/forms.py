from django import forms
from .models import Student

class NewStudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
    # CHOICES = models.Student().course_in_list()

    # student_number = forms.CharField(label='Student Number', max_length=20)
    # first_name = forms.CharField(label='First Name', max_length=120)
    # last_name = forms.CharField(label='Last Name', max_length=120)
    # student_address = forms.CharField(label='Address', max_length=120)
    # course = forms.CharField(label='Course', widget=forms.Select(choices=models.Student().COURSE_IN_SCHOOL))