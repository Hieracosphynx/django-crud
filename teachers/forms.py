from django import forms
from .models import Teacher
from students.models import Student

class NewTeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = '__all__'


class UpdateStudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        exclude = ('student_number',)