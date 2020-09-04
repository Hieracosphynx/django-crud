from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import NewTeacherForm
# Create your views here.
def index(request):
    text = "Pick a method."
    return render(request, 'teachers/index.html', {'intro': text})

def create(request):
    form = NewTeacherForm()
    if request.method == 'GET':
        form = NewTeacherForm()
        return render(request, 'teachers/create.html', {'form': form})
    else: 
        form = NewTeacherForm(request.POST)
        if form.is_valid():
            print('Success')
            form.save()
            return redirect(request.path_info)
        else:
            return HttpResponse(form.errors)
