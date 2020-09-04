from django import forms
from .models import Teacher

class NewTeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = '__all__'