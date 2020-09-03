from django.shortcuts import render, redirect
from django.http import HttpResponse 
from .forms import NewStudentForm
# Create your views here.

def index(request):
    return render(request, 'students/index.html',{})

def create(request):
    form = NewStudentForm()
    # student_db = models.Student()

    if request.method == 'GET':
        form = NewStudentForm()
        return render(request, 'students/create.html', {'form': form})
    else:
        form = NewStudentForm(request.POST)
        if form.is_valid():
            print('Validation Success!')
            form.save()
            return redirect(request.path_info)
    # return render(request, 'students/create.html', {'form': form})