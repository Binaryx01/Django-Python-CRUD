from django.shortcuts import render,redirect,get_object_or_404
from .forms import StudentForm
from .models import Student

# Create your views here.

def index(request):
    if request.method=="POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = StudentForm()

    students = Student.objects.all()
    return render(request,"index.html",{'form':form,'students':students})


def viewdata(request):
    students = Student.objects.all()
    return render(request,'viewdata.html',{'students':students})


def edit_student(request,id):
    student = get_object_or_404(Student,pk=id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('viewdata')  # redirect to list after saving
    else:
        form = StudentForm(instance=student)
    return render(request,'edit_student.html',{'form':form})


def delete_student(request, id):
    student = get_object_or_404(Student, pk=id)
    student.delete()
    return redirect('viewdata')

