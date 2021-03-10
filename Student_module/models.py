from django.db import models
from django.core.validators import RegexValidator, MaxValueValidator, MinValueValidator
# Create your models here.
from django.contrib.auth.models import User

# from Teacher_module.models import Teacher_General_Info

SECTION = (('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'))


class Student_General_Info(models.Model):
    Student_ID = models.AutoField(primary_key=True)
    Roll_No = models.IntegerField()
    Name = models.CharField(max_length=30)
    Father_Name = models.CharField(max_length=30)
    Date_Of_Birth = models.DateField()
    phone_regex = RegexValidator(
        regex=r'^(0)+\d{10}$', message="Phone number must be correct Add 0 at starting")
    Father_Phone_Number = models.CharField(
        validators=[phone_regex], max_length=11)
    Alternate_Number = models.CharField(
        validators=[phone_regex], max_length=11)
    Address = models.TextField(max_length=255)
    Photo = models.ImageField(
        upload_to='Photo', blank=True, default='Photo/default.jpg')

    Blood_Group = models.CharField(max_length=3, blank=True)

    def __int__(self):
        return self.Student_ID


class Student_Academy_Info(models.Model):
    student_ID = models.OneToOneField(
        Student_General_Info, on_delete=models.CASCADE)

    Semester = models.IntegerField(
        validators=[MaxValueValidator(12), MinValueValidator(1)])
    Section = models.CharField(max_length=1, choices=SECTION)

    Branch = models.CharField(max_length=20)
