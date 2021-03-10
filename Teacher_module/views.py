from django.shortcuts import render
from Teacher_module.models import Teacher_General_Info, Teacher_Academy_Info,  Student_Notes, Assignment, Assignment_Submission
from Student_module.models import Student_General_Info, Student_Academy_Info
# Create your views here.
import json
from django.urls import reverse
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from Teacher_module.forms import Student_NotesForm
# Create your views here.


def Notes(request):

    AcademyDetails = []
    username = request.user.username

    AcademyDetails = Teacher_Academy_Info.objects.all().filter(teacher_ID_id=username)
    Subject = []
    Semester = []
    Branch = []
    Section = []
    for Details in AcademyDetails:
        if Details.Subject != None:
            Subject.append(Details.Subject)
        if Details.Semester != None:
            Semester.append(Details.Semester)
        if Details.Branch != None:
            Branch.append(Details.Branch)
        if Details.Section != None:
            Section.append(Details.Section)
    Subject = set(Subject)
    Semester = set(Semester)
    Branch = set(Branch)
    Section = set(Section)

    Details = Student_Notes.objects.all().filter(Teacher_ID_id=username)
    if request.method == 'POST':
        Note = Student_Notes()
        Note.Teacher_ID = Teacher_General_Info(Teacher_ID=username)
        Note.Semester = request.POST.get('Semester')
        Note.Branch = request.POST.get('Branch')
        Note.Section = request.POST.get('Section')
        Note.Subject = request.POST.get('Subject')
        if 'notes' in request.FILES:
            Note.Notes = request.FILES['notes']
        Note.Description = request.POST.get('description')
        Note.save()
        messages.success(request, "Notes are Uploaded Successfully")

    return render(request, 'Teacher/Add_Notes.html', {'Subject': Subject, 'Semester': Semester, 'Branch': Branch, 'Section': Section, 'Details': Details})


def Student_Assignment(request):

    AcademyDetails = []
    username = request.user.username

    AcademyDetails = Teacher_Academy_Info.objects.all().filter(teacher_ID_id=username)
    Subject = []
    Semester = []
    Branch = []
    Section = []
    for Details in AcademyDetails:
        if Details.Subject != None:
            Subject.append(Details.Subject)
        if Details.Semester != None:
            Semester.append(Details.Semester)
        if Details.Branch != None:
            Branch.append(Details.Branch)
        if Details.Section != None:
            Section.append(Details.Section)

    Details = Assignment.objects.all().filter(Teacher_ID_id=username)

    if request.method == 'POST':
        Assignment_Details = Assignment()
        Assignment_Details.Teacher_ID = Teacher_General_Info(
            Teacher_ID=username)
        Assignment_Details.Description = request.POST.get('description')
        Assignment_Details.Semester = request.POST.get('Semester')
        Assignment_Details.Branch = request.POST.get('Branch')
        Assignment_Details.Section = request.POST.get('Section')
        Assignment_Details.Subject = request.POST.get('Subject')
        if 'assignment' in request.FILES:
            Assignment_Details.Question_Paper = request.FILES['assignment']
        Assignment_Details.save()
        messages.success(request, 'Upload Successfully..!!')
    return render(request, 'Teacher/Assignment.html', {'Subject': Subject, 'Semester': Semester, 'Branch': Branch, 'Section': Section, 'Details': Details})


def Submissions(request, id):

    Details = Assignment.objects.get(id=id)
    Submitted = Assignment_Submission.objects.all().filter(Assignment_ID_id=id)
    Not_Submitted = Assignment_Submission.objects.values(
        'Student_ID_id').filter(Assignment_ID_id=id)
    Academy = Student_Academy_Info.objects.all().filter(
        Semester=Details.Semester, Branch=Details.Branch, Section=Details.Section).exclude(student_ID_id__in=Not_Submitted)

    Student = []
    for Detail in Academy:
        Student.append(Student_General_Info.objects.get(
            Student_ID=Detail.student_ID_id))

    return render(request, 'Teacher/Submission.html', {'Submitted': Submitted, 'Student': Student})
