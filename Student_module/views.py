from django.shortcuts import render
from django.contrib import messages
from .models import Student_General_Info, Student_Academy_Info
from Teacher_module.models import Teacher_Academy_Info, Teacher_General_Info, Student_Notes, Assignment, Assignment_Submission

from django.contrib.auth.models import User
# Create your views here.

# Create your views here.


def Profile_Info(request):
    user = request.user.username
    General_Info = Student_General_Info.objects.get(Student_ID=user)
    Academy_Info = Student_Academy_Info.objects.get(student_ID_id=user)
    Info = User.objects.get(username=user)

    return render(request, 'Student/Profile_Info.html', {'Info': Info, 'General_Info': General_Info, 'Academy_Info': Academy_Info})


def StudentNotes(request):
    user = request.user.username
    Student = Student_Academy_Info.objects.get(student_ID_id=user)

    Details = Student_Notes.objects.all().filter(
        Semester=Student.Semester, Branch=Student.Branch, Section=Student.Section)
    print(Details)
    print(Student.Branch, Student.Semester, Student.Section)
    return render(request, 'Student/Notes.html', {'Details': Details})


def AssignmentSubmission(request):
    user = request.user.username
    Student = Student_Academy_Info.objects.get(student_ID_id=user)
    Student_Details = Student_General_Info.objects.get(Student_ID=user)

    Submission = Assignment_Submission.objects.values('Assignment_ID_id').filter(
        Student_ID_id=user)
    print(Submission)
    Details = Assignment.objects.all().filter(
        Semester=Student.Semester, Branch=Student.Branch, Section=Student.Section).exclude(id__in=Submission)
    print(Details)
    if request.method == 'POST':
        Submission = Assignment_Submission()
        Submission.Assignment_ID = Assignment(id=int(request.POST.get('id')))
        Submission.Student_ID = Student_General_Info(Student_ID=user)
        Submission.Semester = Student.Semester
        Submission.Branch = Student.Branch
        Submission.Section = Student.Section
        Submission.Student_Name = Student_Details.Name
        if 'assignment' in request.FILES:
            Submission.Answer_Sheet = request.FILES['assignment']
        Submission.save()
        messages.success(request, "Uploaded Successfully..!!")
    return render(request, 'Student/Assignment.html', {'Details': Details})
