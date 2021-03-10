from django.urls import path

from . import views

app_name = 'Student_module'

urlpatterns = [
    path('Profile_Info/', views.Profile_Info, name='Profile_Info'),
    path('Notes/', views.StudentNotes, name='Notes'),
    path('Assignment/', views.AssignmentSubmission, name='Assignment'),
]
