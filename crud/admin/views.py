from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import logout as auth_logout

@login_required
def dashboard(request):
    return render(request, 'admin/Dashboard.html')

@login_required
def class_teacher_management(request):
    return render(request, 'admin/Class & Teacher Management.html')

@login_required
def user_account(request):
    return render(request, 'admin/User Account.html')

@login_required
def resources_course_materials(request):
    return render(request, 'admin/Resources & Course Materials.html')

@login_required
def system_setting_reports(request):
    return render(request, 'admin/System Setting & Reports.html')

@login_required
def logout_view(request):
    auth_logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('/login/') 