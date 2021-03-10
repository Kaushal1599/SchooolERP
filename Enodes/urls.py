"""Erp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,  include
from . import views
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
urlpatterns = [

    path('', views.user_login, name='login'),
    path('Admin_module/', include('Admin_module.urls')),
    path('Teacher_module/', include('Teacher_module.urls')),
    path('Student_module/', include('Student_module.urls')),
    path('Admin_Dashboard/', views.Admin_Dashboard, name='Admin_Dashboard'),
    path('Teacher_Dashboard/', views.Teacher_Dashboard, name='Teacher_Dashboard'),
    path('Student_Dashboard/', views.Student_Dashboard, name='Student_Dashboard'),
    path('logout/', views.user_logout, name='user_logout'),
    path('Change_Password/', views.Change_Password, name='Change_Password'),
    #path('forget_Password/', views.Forget_Password, name='forget_password')
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='Reset_Password.html'),
         name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name='Reset_Password_Sent.html'),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name='Password_Reset_Confirm.html'),
         name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='Reset_Password_Complete.html'),
         name='password_reset_complete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
