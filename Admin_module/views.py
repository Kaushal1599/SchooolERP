from django.shortcuts import render
from django.contrib.auth.hashers import make_password
# Create your views here.

import json
from django.core import serializers
from django.http import JsonResponse
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import Student_GeneralForm, Student_AcademyForm
from Student_module.models import Student_Academy_Info, Student_General_Info
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
from django.http import HttpResponseRedirect, HttpResponse
from Teacher_module.models import Teacher_General_Info, Teacher_Academy_Info
from .forms import Teacher_GeneralForm


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required
def Create_Student(request):

    if request.method == 'POST':

        Student = Student_GeneralForm(data=request.POST)
        Academy = Student_AcademyForm(data=request.POST)
        email = request.POST.get('email')
        date = request.POST.get('date')

        if Student.is_valid() and Academy.is_valid():
            Academy_info = Academy.save(commit=False)

            user = Student.save(commit=False)
            try:
                check_name = Student_General_Info.objects.get(Name=user.Name)
                check_class = Student_Academy_Info.objects.get(
                    Class=Academy_info.Class)
                if check_name.Father_Name == user.Father_Name:
                    if check_class.Class == Academy_info.Class:
                        messages.error(request, "User Already Exist")
            except Exception as e:
                print(e)

                if 'Photo' in request.FILES:
                    user.Photo = request.FILES['Photo']
                user.Date_Of_Birth = date
                user.save()
                Password = user.Father_Phone_Number[7:]
                Auth = User()
                Auth.username = user.Student_ID
                Auth.set_password(Password)
                Auth.email = email
                Auth.save()

                Academy_info = Academy.save(commit=False)

                Academy_info.student_ID_id = user

                Academy_info.save()
                messages.success(request, 'Student Registered Successfully')
                Student = Student_GeneralForm()
                Academy = Student_AcademyForm()
        else:
            print(Student.errors)
            print(Academy.errors)
    else:
        Student = Student_GeneralForm()
        Academy = Student_AcademyForm()
    return render(request, 'Admin/Add_Student.html', {'Student': Student, 'Academy': Academy})


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required
def Create_Teacher(request):

    if request.method == 'POST':
        Teacher = Teacher_GeneralForm(data=request.POST)
        Subject = request.POST.getlist('Subject[]')
        Semester = request.POST.getlist('Semester[]')
        Branch = request.POST.getlist('Branch[]')
        Section = request.POST.getlist('Section[]')

        email = request.POST.get('email')
        if Teacher.is_valid():
            user = Teacher.save(commit=False)

            if 'Photo' in request.FILES:
                user.Photo = request.FILES['Photo']

            user.save()
            Password = user.Teacher_Phone_Number[7:]
            Auth = User()
            Auth.username = user.Teacher_ID
            Auth.set_password(Password)
            Auth.email = email
            Auth.save()

            i = 0

            while(i < len(Subject)):
                Academy = Teacher_Academy_Info()
                Academy.Subject = Subject[i]
                Academy.Semester = int(Semester[i])
                Academy.Branch = Branch[i]
                Academy.Section = Section[i]
                Academy.teacher_ID_id = user.Teacher_ID
                Academy.save()
                i += 1

            Academy.save()
            Teacher = Teacher_GeneralForm()
            messages.success(request, 'Teacher Registered Successfully')
        else:
            print(Teacher.errors)

    else:
        Teacher = Teacher_GeneralForm()

    return render(request, "Admin/Add_Teacher.html", {'Teacher': Teacher})
