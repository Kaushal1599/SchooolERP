from django.db import models
from django.core.validators import RegexValidator
from django.core.validators import MaxValueValidator, MinValueValidator
from Student_module.models import Student_General_Info
# Create your models here

SECTION = (('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'))


class Teacher_General_Info(models.Model):
    Teacher_ID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=20)
    phone_regex = RegexValidator(
        regex=r'^(0)+\d{10}$', message="Phone number must be correct Add 0 at starting")
    Teacher_Phone_Number = models.CharField(
        validators=[phone_regex], max_length=11)
    Address = models.TextField(max_length=50)
    Qualification = models.CharField(max_length=20)
    Photo = models.ImageField(
        upload_to='photo', blank=True, default='Photo/default.jpg')

    def __init_(self):
        return self.Teacher_ID


class Teacher_Academy_Info(models.Model):
    teacher_ID = models.ForeignKey(
        Teacher_General_Info, on_delete=models.CASCADE)

    Subject = models.CharField(max_length=15, blank=True)
    Semester = models.IntegerField(
        validators=[MaxValueValidator(12), MinValueValidator(1)], blank=True)
    Branch = models.CharField(max_length=20)
    Section = models.CharField(max_length=1, blank=True)


class Student_Notes(models.Model):
    Teacher_ID = models.ForeignKey(
        Teacher_General_Info, on_delete=models.CASCADE)
    Semester = models.IntegerField(
        validators=[MaxValueValidator(12), MinValueValidator(1)])
    Branch = models.CharField(max_length=20)
    Section = models.CharField(max_length=1, choices=SECTION)
    Subject = models.CharField(max_length=15)
    Notes = models.FileField(upload_to='Notes')
    Description = models.TextField(max_length=50)


class Assignment(models.Model):
    Description = models.TextField(max_length=50)
    Question_Paper = models.FileField(upload_to='Question')
    Semester = models.IntegerField(
        validators=[MaxValueValidator(12), MinValueValidator(1)])
    Branch = models.CharField(max_length=20)
    Section = models.CharField(choices=SECTION, max_length=1)
    Subject = models.CharField(max_length=15)
    Teacher_ID = models.ForeignKey(
        Teacher_General_Info, on_delete=models.CASCADE)


class Assignment_Submission(models.Model):
    Assignment_ID = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    Student_ID = models.ForeignKey(
        Student_General_Info, on_delete=models.CASCADE)
    Semester = models.IntegerField(
        validators=[MaxValueValidator(12), MinValueValidator(1)])
    Branch = models.CharField(max_length=20)
    Section = models.CharField(choices=SECTION, max_length=1)
    Student_Name = models.CharField(max_length=20, blank=True)
    Answer_Sheet = models.FileField(upload_to='Answer', blank=True)
