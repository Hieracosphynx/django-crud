from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import NewTeacherForm, UpdateStudentForm
from  students.models import Student
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

def listStudents(request):
    students = Student.objects.order_by('last_name')
    my_dict = {'students': students}
    return render(request, 'teachers/list.html', context = my_dict)

def update(request, id):
    student = Student.objects.get(pk=id)


    form = UpdateStudentForm()
    
    if request.method == 'GET':
        print(request.method)
        form = UpdateStudentForm()
        form = UpdateStudentForm(initial={'student_number': student.student_number, 
                                        'first_name': student.first_name, 
                                        'last_name': student.last_name, 
                                        'student_address': student.student_address,
                                        'course': student.course})
        
        my_dict = {'student': student, 'form': form}
        return render(request, 'teachers/update.html', context = my_dict)
    else:
        print(request.method)
        # student = Student.objects.get(pk=id)
        # my_dict = {'student': student}
        # return render(request, 'teachers/update.html', context = my_dict)

    