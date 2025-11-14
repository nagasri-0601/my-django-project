from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Student 

def home(request):
    return render(request, 'index.html')

def add_student(request):
    if request.method == 'POST':
        name = request.POST['name']
        age = request.POST['age']
        email = request.POST['email']

        Student.objects.create(name=name, age=age, email=email)

        return redirect('show_students')  

    return render(request, 'add_student.html')

def show_students(request):
    students = Student.objects.all()
    return render(request, 'show_students.html', {'students': students})
