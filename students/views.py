from django.shortcuts import render
from django.http import HttpResponse 
from . import forms, models
# Create your views here.

def index(request):
    return render(request, 'students/index.html',{})

def create(request):
    form = forms.NewStudentForm()
    courses = models.Student()
    c = courses.course_in_list

    if request.method == 'POST':
        form = forms.NewStudentForm(request.POST)
        if form.is_valid():
            print('Validation Success!')
    return render(request, 'students/create.html', {'form': form, 'd': c})