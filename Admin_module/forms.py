from django import forms
from Student_module.models import Student_General_Info, Student_Academy_Info
from Teacher_module.models import Teacher_Academy_Info, Teacher_General_Info
from django.forms import modelformset_factory
from django.contrib.auth.models import User

from django.contrib.admin.widgets import AdminDateWidget

TERM = (('SA-1', 'SA-1'), ('SA-2', 'SA-2'), ('FA-1', 'FA-1'), ('FA-2', 'FA-2'),
        ('FA-3', 'FA-3'), ('FA-4', 'FA-4'), ('Class Test', 'Class Test'))

SECTION = (('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'))


class Student_GeneralForm(forms.ModelForm):

    class Meta:
        model = Student_General_Info
        fields = ('Name', 'Roll_No', 'Father_Name', 'Father_Phone_Number', 'Alternate_Number',
                  'Address', 'Photo', 'Blood_Group',)


class Student_AcademyForm(forms.ModelForm):
    Section = forms.ChoiceField(choices=SECTION, required=True)

    class Meta:
        model = Student_Academy_Info
        fields = ('Semester', 'Branch', 'Section')


class Teacher_GeneralForm(forms.ModelForm):
    email = forms.CharField(widget=forms.EmailInput())

    class Meta:
        model = Teacher_General_Info
        fields = '__all__'
