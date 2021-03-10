from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.urls import reverse
from Teacher_module.models import Teacher_General_Info
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
from django.contrib.auth.hashers import check_password
from django.contrib import messages
# from django.contrib import messages
from django.contrib.auth.models import User
from Teacher_module.models import Teacher_Academy_Info
from Student_module.models import Student_General_Info


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def user_login(request):
    userID = request.user.username
    if userID == "":

        if request.method == "POST":

            username = request.POST.get('ID')
            password = request.POST.get('password')

            user = authenticate(username=username, password=password)

            try:
                if username.isdigit():
                    username = int(username)
                    if username < 1000:
                        if user.is_active:

                            login(request, user)

                            return HttpResponseRedirect(reverse('Teacher_Dashboard'))
                    elif user.is_active:

                        login(request, user)

                        return HttpResponseRedirect(reverse('Student_Dashboard'))
                elif user.is_active:

                    login(request, user)

                    return HttpResponseRedirect(reverse('Admin_Dashboard'))
            except Exception as e:
                print(e)
                messages.error(request, "Invalid Details")
    else:
        if userID.isdigit():
            userID = int(userID)
            if userID < 1000:

                return HttpResponseRedirect(reverse('Teacher_Dashboard'))
            else:

                return HttpResponseRedirect(reverse('Student_Dashboard'))
        else:

            return HttpResponseRedirect(reverse('Admin_Dashboard'))

    # if (session_variable == False):
    return render(request, 'login.html')


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required
def Admin_Dashboard(request):

    return render(request, 'Admin/Dashboard.html')


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required
def Teacher_Dashboard(request):

    username = request.user.username
    Basic_Info = Teacher_General_Info.objects.get(Teacher_ID=username)

    return render(request, 'Teacher/Dashboard.html', {'Basic_Info': Basic_Info})


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required
def Student_Dashboard(request):

    username = request.user.username
    Basic_Info = Student_General_Info.objects.get(Student_ID=username)
    return render(request, 'Student/Dashboard.html', {'Basic_Info': Basic_Info})


def Change_Password(request):
    isTeacher = False
    isStudent = False
    isAdmin = False
    username = request.user.username
    if username.isdigit():
        username = int(username)
        if username < 1000:
            isTeacher = True
        else:
            isStudent = True
    else:
        isAdmin = True
    user = User.objects.get(username=username)
    if request.method == 'POST':
        current = request.POST.get('Current_Password')
        new = request.POST.get('New_Password')
        confirm = request.POST.get('Confirm_Password')
        if check_password(current, user.password):
            if new == confirm:
                user.set_password(new)
                user.save()
                messages.success(request, "Password Updated Successfully")
                return HttpResponseRedirect(reverse('login'))
            else:
                messages.error(request, "Password did not match")
        else:
            messages.error(request, "Current Password is wrong")

    return render(request, 'Change_Password.html', {'isTeacher': isTeacher, 'isStudent': isStudent, 'isAdmin': isAdmin})


def Forget_Password(request):
    if request.method == 'POST':
        username = request.POST.get('Username')
        new = request.POST.get('New_Password')
        confirm = request.POST.get('Confirm_Password')
        try:
            user = User.objects.get(username=username)

            if new == confirm:
                user.set_password(new)
                user.save()
                messages.success(request, "Password Updated Successfully")
                return HttpResponseRedirect(reverse('login'))
            else:
                messages.error(request, "Password did not match")
        except Exception as e:
            print(e)
            messages.error(request, "No user found")

    return render(request, 'Forget_Password.html')
