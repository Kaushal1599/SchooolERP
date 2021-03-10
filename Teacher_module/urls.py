from django.urls import path
from . import views
app_name = 'Teacher_module'

urlpatterns = [
    path('Add_Notes/', views.Notes, name='Add_Notes'),
    path('Assignment/', views.Student_Assignment, name='Assignment'),
    path('Submission/<int:id>', views.Submissions, name='Submission'),

]
