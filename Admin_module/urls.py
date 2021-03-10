from django.urls import path

from Admin_module import views

app_name = 'Admin_module'
urlpatterns = [
    path('Create_Student/', views.Create_Student, name='Create_Student'),
    path('Create_Teacher/', views.Create_Teacher, name='Create_Teacher'),


]
