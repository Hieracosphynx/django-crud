from django.shortcuts import render, redirect
from .forms import NewTeacherForm
# Create your views here.
def index(request):
    text = "Pick a method."
    return render(request, 'teachers/index.html', {'intro': text})

def create(request):
    if request.method == 'GET':
        form = NewTeacherForm()
        return render(request, 'teachers/create', {'form': form})
    else: 
        form = NewTeacherForm(request.POST)
        if form.is_valid():
            print('Success')
            form.save()
            return redirect(request.path_info)
