from django import forms
from .models import Teacher

class NewTeacherForm(forms.Form):
    class Meta:
        model = Teacher
        fields = '__all__'