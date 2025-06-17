from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from .models import  Student, AssignedTask, Task, Teacher, Section
from django.http import HttpResponse, JsonResponse
from django.core.paginator import Paginator
from django.db.models import Q, F
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.sessions.models import Session
from functools import wraps
from django.http import HttpResponseRedirect
from django.urls import reverse
import re
from datetime import date, datetime, timedelta
from django.utils import timezone
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags
import json
import calendar
import os

def student_login_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if not request.session.get('is_student_authenticated'):
            return HttpResponseRedirect(reverse('login'))
        return view_func(request, *args, **kwargs)
    return _wrapped_view

def teacher_login_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if not request.session.get('is_teacher_authenticated'):
            return HttpResponseRedirect(reverse('login'))
        return view_func(request, *args, **kwargs)
    return _wrapped_view

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Try student login first
        try:
            student = Student.objects.get(username=username)
            if check_password(password, student.password):
                request.session['student_id'] = student.student_id
                request.session['student_username'] = student.username
                request.session['is_student_authenticated'] = True
                messages.success(request, f'Welcome {student}!')
                return redirect('student_dashboard')
            else:
                # If password doesn't match, try teacher login
                try:
                    teacher = Teacher.objects.get(username=username)
                    if check_password(password, teacher.password):
                        request.session['teacher_id'] = teacher.teacher_id
                        request.session['teacher_username'] = teacher.username
                        request.session['is_teacher_authenticated'] = True
                        messages.success(request, f'Welcome {teacher}!')
                        return redirect('teacher_dashboard')
                    else:
                        messages.error(request, 'Invalid username or password.')
                except Teacher.DoesNotExist:
                    messages.error(request, 'Invalid username or password.')
        except Student.DoesNotExist:
            # If student not found, try teacher login
            try:
                teacher = Teacher.objects.get(username=username)
                if check_password(password, teacher.password):
                    request.session['teacher_id'] = teacher.teacher_id
                    request.session['teacher_username'] = teacher.username
                    request.session['is_teacher_authenticated'] = True
                    messages.success(request, f'Welcome {teacher}!')
                    return redirect('teacher_dashboard')
                else:
                    messages.error(request, 'Invalid username or password.')
            except Teacher.DoesNotExist:
                messages.error(request, 'Invalid username or password.')

    return render(request, 'layout/Login.html')

def student_logout(request):
    request.session.flush()
    messages.success(request, 'You have been logged out successfully.')
    return redirect('login')

def teacher_logout(request):
    request.session.flush()
    messages.success(request, 'You have been logged out successfully.')
    return redirect('login')

@student_login_required
def student_dashboard(request):
    try:
        # Get search input
        search_query = request.GET.get('search', '')
        
        # Calendar functionality
        import calendar
        from datetime import datetime, timedelta
        
        # Get the current month or use the month from the request
        month_str = request.GET.get('month')
        if month_str:
            current_month = datetime.strptime(month_str, '%Y-%m')
        else:
            current_month = datetime.now()
            
        # Calculate previous and next months
        prev_month = current_month - timedelta(days=1)
        next_month = current_month + timedelta(days=32)
        
        # Get the calendar for the current month
        cal = calendar.monthcalendar(current_month.year, current_month.month)
        
        # Get all tasks with deadlines for the current month
        student_id = request.session.get('student_id')
        tasks_with_deadlines = AssignedTask.objects.filter(
            student_id=student_id,
            task__deadline__year=current_month.year,
            task__deadline__month=current_month.month
        ).select_related('task')
        
        # Create a dictionary of days with deadlines
        deadline_days = {}
        now = datetime.now()
        for task in tasks_with_deadlines:
            day = task.task.deadline.day
            if day not in deadline_days:
                deadline_days[day] = []
            
            # Determine deadline status
            deadline = task.task.deadline
            if deadline < now:
                status = 'overdue'
            elif (deadline - now).days <= 3:  # Within 3 days
                status = 'urgent'
            else:
                status = 'upcoming'
                
            deadline_days[day].append({
                'title': task.task.title,
                'deadline': task.task.deadline,
                'status': status
            })
        
        # Flatten the calendar and add deadline information
        calendar_days = []
        for week in cal:
            for day in week:
                if day == 0:
                    calendar_days.append(0)
                else:
                    tasks = deadline_days.get(day, [])
                    # Determine the most urgent status for the day
                    status = 'normal'
                    if tasks:
                        if any(task['status'] == 'overdue' for task in tasks):
                            status = 'overdue'
                        elif any(task['status'] == 'urgent' for task in tasks):
                            status = 'urgent'
                        else:
                            status = 'upcoming'
                            
                    calendar_days.append({
                        'day': day,
                        'has_deadline': day in deadline_days,
                        'tasks': tasks,
                        'status': status
                    })

        # Start with all assigned tasks
        assigned_tasks = AssignedTask.objects.filter(student_id=student_id)

        # Filter results if search is entered
        if search_query:
            assigned_tasks = assigned_tasks.filter(
                Q(student__last_name__icontains=search_query) |
                Q(student__first_name__icontains=search_query) |
                Q(student__middle_name__icontains=search_query) |
                Q(student__suffix__icontains=search_query) |
                Q(task__title__icontains=search_query)
            )

        # Pagination: Show 6 items per page
        paginator = Paginator(assigned_tasks, 8)
        page_number = request.GET.get('page', 1)
        page_obj = paginator.get_page(page_number)

        data = {
            'assigned_tasks': page_obj,
            'page_obj': page_obj,
            'search_query': search_query,
            'calendar': calendar_days,
            'current_month': current_month,
            'prev_month': prev_month,
            'next_month': next_month,
            'today': datetime.now()
        }

        return render(request, 'student/dashboard.html', data)

    except Exception as e:
        return HttpResponse(f'Error: {e}')

    # return render(request, "student/dashboard.html")

@student_login_required
def student_course_material(request):
    try:
        # Get search input
        search_query = request.GET.get('search', '')
        student_id = request.session.get('student_id')
        # Start with all gender data
        assigned_tasks = AssignedTask.objects.filter(student_id=student_id)

        # Filter results if search is entered
        if search_query:
            assigned_tasks = assigned_tasks.filter(
                Q(teacher__last_name__icontains=search_query) |
                Q(teacher__first_name__icontains=search_query) |
                Q(teacher__middle_name__icontains=search_query) |
                Q(teacher__suffix__icontains=search_query) |
                Q(task_title__icontains=search_query) 
            )
              # assuming your model has a 'name' field

        # Pagination: Show 6 items per page
        paginator = Paginator(assigned_tasks, 8)
        page_number = request.GET.get('page', 1)
        page_obj = paginator.get_page(page_number)

        data = {
            'assigned_tasks': page_obj,
            'page_obj': page_obj,
            'search_query': search_query
        }

        return render(request, "student/course_material.html", data)

    except Exception as e:
        return HttpResponse(f'Error: {e}')

@student_login_required
def task_description(request, id):
    try:
        task = Task.objects.get(pk=id)
        task = {'task':task}
        return render(request,'student/task_description.html',  task)
    except Exception as e:
        return HttpResponse(f'Error: {e}')

@student_login_required
def student_assignments_exams(request):
    student_id = request.session.get('student_id')
    assigned_tasks = AssignedTask.objects.filter(student_id=student_id).select_related('task')

    # Add submission status for each assigned task
    for assigned_task in assigned_tasks:
        if assigned_task.status == 'submitted' and assigned_task.task.deadline and assigned_task.submitted_at:
            if assigned_task.submitted_at <= assigned_task.task.deadline:
                assigned_task.submission_status = 'On Time'
            else:
                assigned_task.submission_status = 'Late'
        elif assigned_task.status == 'pending':
            assigned_task.submission_status = 'Pending'
        elif assigned_task.status == 'graded':
            if assigned_task.task.deadline and assigned_task.submitted_at:
                if assigned_task.submitted_at <= assigned_task.task.deadline:
                    assigned_task.submission_status = 'Graded (On Time)'
                else:
                    assigned_task.submission_status = 'Graded (Late)'
            else:
                assigned_task.submission_status = 'Graded'
        else:
            assigned_task.submission_status = assigned_task.status # Fallback for other statuses

    if request.method == 'POST':
        assigned_task_id = request.POST.get('assigned_task_id')
        assignment_file = request.FILES.get('assignment_file')

        if not assigned_task_id or not assignment_file:
            messages.error(request, "Please select a subject and upload a file.")
            return redirect('/student/assignments-exams/')  # Use your URL name

        try:
            assigned_task = AssignedTask.objects.get(id=assigned_task_id, student_id=student_id)
            assigned_task.submission_file = assignment_file
            assigned_task.status = 'submitted'
            assigned_task.submitted_at = timezone.now()
            assigned_task.save()

            messages.success(request, "Assignment submitted successfully!")
        except AssignedTask.DoesNotExist:
            messages.error(request, "Invalid assignment selection.")

        assigned_tasks = AssignedTask.objects.filter(student_id=student_id)
        return redirect('/student/assignments-exams/' )  # Use your URL name
    has_pending = any(task.status == 'pending' for task in assigned_tasks)
    return render(request, 'student/assignments_exams.html', {
    'assigned_tasks': assigned_tasks,
    'has_pending': has_pending,})

# def student_assignments_exams(request):

#     try:
#         student_id = request.session.get('student_id')
#         assigned_tasks = AssignedTask.objects.filter(student_id=student_id)
#         assigned_tasks = {
#             'assigned_tasks':assigned_tasks
#         }
#         return render(request, "student/assignments_exams.html",assigned_tasks)
#     except Exception as e:
#             return HttpResponse(f'Error: {e}')
    

@student_login_required
def student_classroom_discussion(request):
    return render(request, "student/classroom_discussion.html")


@student_login_required
def student_profile_settings(request):
    try:
        student_id = request.session.get('student_id')
        student = Student.objects.get(student_id=student_id)
        student = {
            'student':student
        }
        return render(request, "student/profile_settings.html",student)
    except Exception as e:
            return HttpResponse(f'Error: {e}')

@student_login_required
def edit_student(request, student_id):
    try:
        if request.method == 'POST':
            # student_id = request.session.get('student_id')
            # student = Student.objects.get(student_id=student_id)

            studentObj = Student.objects.get(pk=student_id)

            
            username = request.POST.get('username')
            first_name = request.POST.get('first_name')
            middle_name = request.POST.get('middle_name')
            last_name = request.POST.get('last_name')
            suffix = request.POST.get('suffix')
            gender = request.POST.get('gender')
            birth_date = request.POST.get('birth_date')
            contact_number = request.POST.get('contact_number')
            email = request.POST.get('email')
            address = request.POST.get('address')
            
            if Student.objects.filter(username=username).exclude(student_id=student_id).exists():
                messages.error(request, 'Username already exists. Please choose a different username.')
                return redirect(f'/student/edit_student/{student_id}')
            
            
            studentObj.first_name = first_name
            studentObj.middle_name = middle_name
            studentObj.last_name = last_name
            studentObj.suffix = suffix
            studentObj.username = username
            studentObj.gender = gender
            studentObj.birth_date = birth_date
            studentObj.contact_number = contact_number
            studentObj.email = email
            studentObj.address = address
            studentObj.save()

            messages.success(request, 'Student updated successfully!')
            return redirect('/student/profile-settings/')
        else:
            studentObj = Student.objects.get(pk=student_id)
            
            data = {
                'student': studentObj,
            }
            
            return render(request,'student/edit_student.html', data)
    except Exception as e:
        messages.error(request, f'An error occurred: {str(e)}')
        return redirect('/student/profile-settings')

@student_login_required
def check_password_strength(password):
    strength = 0
    feedback = []
    if len(password) >= 8:
        strength += 1
    else:
        feedback.append('At least 8 characters')
    if re.search(r'[a-z]', password):
        strength += 1
    else:
        feedback.append('Lowercase letter')
    if re.search(r'[A-Z]', password):
        strength += 1
    else:
        feedback.append('Uppercase letter')
    if re.search(r'[0-9]', password):
        strength += 1
    else:
        feedback.append('Number')
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        strength += 1
    else:
        feedback.append('Special character')
    return strength, feedback


@student_login_required
def student_changepass(request,student_id):
    # if request.method == 'POST':
    #     new_password = request.POST.get('new_password')
    #     confirm_password = request.POST.get('confirm_password')

    #     if new_password != confirm_password:
    #         messages.error(request, 'New password and confirm password do not match!')
    #         return redirect('/student/student_changepass/')

    #     strength, feedback = check_password_strength(new_password)
    #     if strength < 3:
    #         messages.error(request, 'Password is too weak. Please make sure it meets all requirements: ' + ', '.join(feedback))
    #         return redirect('/student/student_changepass/')

    #     # Save the new password here (hash it!)
    #     # user.set_password(new_password)
    #     # user.save()
    #     messages.success(request, 'Password changed successfully!')
    #     return redirect('/student/profile_settings/')

    # return render(request, 'student/student_changepass.html')

    try:
        if request.method == 'POST':
            student = Student.objects.get(pk=student_id)
            current_password = request.POST.get('current_password')
            password = request.POST.get('password')
            confirmPassword = request.POST.get('confirm_password')

            # First verify the current password
            if not check_password(current_password, student.password):
                messages.error(request, 'Current password is incorrect.')
                return redirect(f'/student/student_changepass/{student_id}')

            if not password or not confirmPassword:
                messages.error(request, 'Please fill out both new password fields.')
                return redirect(f'/student/student_changepass/{student_id}')

            if password != confirmPassword:
                messages.error(request, 'New password and confirm password do not match!')
                return redirect(f'/student/student_changepass/{student_id}')

            student.password = make_password(password)
            student.save()
            messages.success(request, 'Password changed successfully!')
            return redirect('/student/profile-settings/')
        else:
            student = Student.objects.get(pk=student_id)
            return render(request, 'student/student_changepass.html', {'student': student})
    except Student.DoesNotExist:
        messages.error(request, "User not found.")
        return redirect('/student/profile-settings/')
    except Exception as e:
        messages.error(request, f"Error changing password: {e}")
        return redirect('/student/profile-settings/')
    

 





def calculate_age(birth_date):
    today = date.today()
    return today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))









# landing page
def landing_page(request):
    return render(request, 'layout/LandingPage.html')

def teacher_registration(request):
    try:
        if request.method == 'POST':
            first_name = request.POST.get('first_name')
            middle_name = request.POST.get('middle_name')
            last_name = request.POST.get('last_name')
            suffix = request.POST.get('suffix')
            gender = request.POST.get('gender')
            birth_date = request.POST.get('birth_date')
            address = request.POST.get('address')
            contact_number = request.POST.get('contact_number')
            email = request.POST.get('email')
            username = request.POST.get('username')
            password = request.POST.get('password')
            confirmPassword = request.POST.get('confirm_password')

            

            
            if password != confirmPassword:
                messages.error(request, 'Password and Confirm Password do not match!')
                data = {
                    'genders': gender,
                    'first_name': first_name,
                    'middle_name': middle_name,
                    'last_name': last_name,
                    'suffix': suffix,
                    'gender': gender,
                    'birth_date': birth_date,
                    'address': address,
                    'contact_number': contact_number,
                    'email': email,
                    'username': username
                }
                return render(request, 'layout/teacher_registration.html', data)
            
            # Check if username already exists
            if Teacher.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists. Please choose a different username.')
                data = {
                    'genders': gender,
                    'first_name': first_name,
                    'middle_name': middle_name,
                    'last_name': last_name,
                    'suffix': suffix,
                    'gender': gender,
                    'birth_date': birth_date,
                    'address': address,
                    'contact_number': contact_number,
                    'email': email,
                    'username': username
                }
                return render(request, 'layout/teacher_registration.html', data)
            

            birth_date_str = birth_date  # e.g., '2000-05-15'
            birth_date_1 = datetime.strptime(birth_date_str, '%Y-%m-%d').date()
            age = calculate_age(birth_date_1)

            Teacher.objects.create(
                    first_name=first_name,
                    middle_name=middle_name,
                    last_name=last_name,
                    suffix=suffix,
                    gender=gender,
                    birth_date=birth_date,
                    age=age,
                    address=address,
                    contact_number=contact_number,
                    email=email,
                    username=username,
                    password=make_password(password)
                    ).save


            messages.success(request, 'Teacher added!')
            teacher = Teacher.objects.get(username=username)
            request.session['teacher_id'] = teacher.teacher_id
            request.session['teacher_username'] = teacher.username
            request.session['is_teacher_authenticated'] = True
            messages.success(request, f'Welcome {teacher}!')
            return redirect('teacher_dashboard') 
        else:
            return render(request,'layout/teacher_registration.html')
    except Exception as e:
        return HttpResponse(f'Error: {e}')












def teacher_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        try:
            teacher = Teacher.objects.get(username=username)
            if check_password(password, teacher.password):
                # Set session data
                request.session['teacher_id'] = teacher.teacher_id
                request.session['teacher_username'] = teacher.username
                request.session['is_teacher_authenticated'] = True
                messages.success(request, f'Welcome {teacher}!')
                return redirect('teacher_dashboard')  # Use your dashboard URL name
            else:
                messages.error(request, f'Invalid username or password.')
        except Teacher.DoesNotExist:
            messages.error(request, 'Username not found.')

    return render(request, 'teacher/Login.html')

@teacher_login_required
def teacher_dashboard(request):
    try:
        teacher_id = request.session.get('teacher_id')
        selected_section = request.GET.get('section')
        search_query = request.GET.get('search', '')
        
        # Get all tasks for the current teacher
        tasks = Task.objects.filter(teacher_id=teacher_id)
        
        # Get all assigned tasks for these tasks
        assigned_tasks = AssignedTask.objects.filter(task__in=tasks).select_related('student', 'task')
        
        # Add submission status for each assigned task
        for assigned_task in assigned_tasks:
            if assigned_task.status == 'submitted' and assigned_task.task.deadline and assigned_task.submitted_at:
                if assigned_task.submitted_at <= assigned_task.task.deadline:
                    assigned_task.submission_status = 'On Time'
                else:
                    assigned_task.submission_status = 'Late'
            elif assigned_task.status == 'pending':
                assigned_task.submission_status = 'Pending'
            elif assigned_task.status == 'graded':
                if assigned_task.task.deadline and assigned_task.submitted_at:
                    if assigned_task.submitted_at <= assigned_task.task.deadline:
                        assigned_task.submission_status = 'Graded (On Time)'
                    else:
                        assigned_task.submission_status = 'Graded (Late)'
                else:
                    assigned_task.submission_status = 'Graded'
            else:
                assigned_task.submission_status = assigned_task.status # Fallback for other statuses

        # Filter by section if selected
        if selected_section:
            # Map section values to section names
            section_map = {
                "1": "A",
                "2": "B",
                "3": "C",
                "4": "D"
            }
            section_name = section_map.get(selected_section)
            if section_name:
                assigned_tasks = assigned_tasks.filter(section__name=section_name)
        
        
        if search_query:
            assigned_tasks = assigned_tasks.filter(
                Q(student__student_id__icontains=search_query) |
                Q(student__first_name__icontains=search_query) |
                Q(student__last_name__icontains=search_query) |
                Q(student__middle_name__icontains=search_query) |
                Q(student__username__icontains=search_query) |
                Q(task__title__icontains=search_query)
            )
        
        
        on_time_passed = assigned_tasks.filter(
            status='submitted',
            submitted_at__lte=F('task__deadline')
        ).count()
        
        late_passed = assigned_tasks.filter(
            status='submitted',
            submitted_at__gt=F('task__deadline')
        ).count()
        
        
        pending_tasks = assigned_tasks.filter(status='pending').count()
        
        
        total_tasks = assigned_tasks.count()
        
        
        total_students = 30

        context = {
            'assigned_tasks': assigned_tasks,
            'on_time_passed': on_time_passed,
            'late_passed': late_passed,
            'pending_tasks': pending_tasks,
            'total_tasks': total_tasks,
            'selected_section': selected_section,
            'search_query': search_query,
            'total_students': total_students
        }
        
        return render(request, "teacher/dashboard.html", context)
    except Exception as e:
        return HttpResponse(f'Error: {e}')

def teacher_assignment(request):
    return render(request, "teacher/assignment.html")

def teacher_student(request):
    try:
        search_query = request.GET.get('search', '')
        students = Student.objects.all().order_by('last_name')

        if search_query:
            students = students.filter(
                Q(first_name__icontains=search_query) |
                Q(last_name__icontains=search_query) |
                Q(username__icontains=search_query) |
                Q(gender__icontains=search_query) |
                Q(email__icontains=search_query) 
            )
            

        paginator = Paginator(students, 8)
        page_number = request.GET.get('page', 1)
        page_obj = paginator.get_page(page_number)

        data = {
            'students': page_obj,
            'page_obj': page_obj,
            'search_query': search_query
        }

        return render(request, 'teacher/student_list.html', data)

    except Exception as e:
        return HttpResponse(f'Error: {e}') 
    

def add_student(request):
    try:
        if request.method == 'POST':
            first_name = request.POST.get('first_name')
            middle_name = request.POST.get('middle_name')
            last_name = request.POST.get('last_name')
            suffix = request.POST.get('suffix')
            gender = request.POST.get('gender')
            birth_date = request.POST.get('birth_date')
            address = request.POST.get('address')
            contact_number = request.POST.get('contact_number')
            email = request.POST.get('email')
            username = request.POST.get('username')
            password = request.POST.get('password')
            confirmPassword = request.POST.get('confirm_password')
            section = request.POST.get('section')

            
            if password != confirmPassword:
                messages.error(request, 'Password and Confirm Password do not match!')
                student = {
                    'genders': gender,
                    'first_name': first_name,
                    'middle_name': middle_name,
                    'last_name': last_name,
                    'suffix': suffix,
                    'gender': gender,
                    'birth_date': birth_date,
                    'address': address,
                    'contact_number': contact_number,
                    'email': email,
                    'username': username,
                    'section': Section.objects.all()
                }
                return render(request, 'teacher/add_student.html', {'student':student})
            
            if Student.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists. Please choose a different username.')
                student = {
                    'genders': gender,
                    'first_name': first_name,
                    'middle_name': middle_name,
                    'last_name': last_name,
                    'suffix': suffix,
                    'gender': gender,
                    'birth_date': birth_date,
                    'address': address,
                    'contact_number': contact_number,
                    'email': email,
                    'username': username,
                    'section': Section.objects.all()
                }
                return render(request, 'layout/teacher_registration.html', {'student':student})
            

            birth_date_str = birth_date  
            birth_date_1 = datetime.strptime(birth_date_str, '%Y-%m-%d').date()
            age = calculate_age(birth_date_1)

            Student.objects.create(
                    first_name=first_name,
                    middle_name=middle_name,
                    last_name=last_name,
                    suffix=suffix,
                    gender=gender,
                    birth_date=birth_date,
                    age=age,
                    address=address,
                    contact_number=contact_number,
                    email=email,
                    username=username,
                    password=make_password(password),
                    section= Section.objects.get(pk=section)
                    ).save


            messages.success(request, 'Student added!')
            return redirect('/teacher/student_list/') 
        else:

            sectionObj = Section.objects.all()

            return render(request, 'teacher/add_student.html', {'sections':sectionObj})
    except Exception as e:
        return HttpResponse(f'Error: {e}')
    

def edit_student1(request,id):
    try:
        if request.method == 'POST':
         
            studentObj = Student.objects.get(pk=id)

            
            username = request.POST.get('username')
            first_name = request.POST.get('first_name')
            middle_name = request.POST.get('middle_name')
            last_name = request.POST.get('last_name')
            suffix = request.POST.get('suffix')
            gender = request.POST.get('gender')
            birth_date = request.POST.get('birth_date')
            contact_number = request.POST.get('contact_number')
            email = request.POST.get('email')
            address = request.POST.get('address')
            section = request.POST.get('section')
            
            if Student.objects.filter(username=username).exclude(student_id=id).exists():
                messages.error(request, 'Username already exists. Please choose a different username.')
                return redirect(f'/student/edit_student/{id}')
            
            
            studentObj.first_name = first_name
            studentObj.middle_name = middle_name
            studentObj.last_name = last_name
            studentObj.suffix = suffix
            studentObj.username = username
            studentObj.gender = gender
            studentObj.birth_date = birth_date
            studentObj.contact_number = contact_number
            studentObj.email = email
            studentObj.address = address
            studentObj.section=Section.objects.get(pk=section)
            studentObj.save()

            messages.success(request, 'Student updated successfully!')
            return redirect('/teacher/student_list/')
        else:
            studentObj = Student.objects.get(pk=id)
            sections = Section.objects.all()
            data = {
                'student': studentObj,
                'sections': sections,
            }
            
            return render(request, 'teacher/edit_student.html', data)
    except Exception as e:
        messages.error(request, f'An error occurred: {str(e)}')
        return redirect('/teacher/student_list/')
    
    
def delete_student1(request, id):
    try:
        if request.method == 'POST':
            student = Student.objects.get(pk=id)
            student_name = f"{student.first_name} {student.last_name}"
            student.delete()
            
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({
                    'success': True, 
                    'message': f'Student "{student_name}" has been deleted successfully!'
                })
            
            messages.success(request, f'Student "{student_name}" has been deleted successfully!')
            return redirect('/teacher/student_list/')
        else:
            student = Student.objects.get(pk=id)
            data = {
                'student': student
            }
            return render(request, 'teacher/delete_student.html', data)
    except Student.DoesNotExist:
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({'success': False, 'error': 'Student not found.'})
        messages.error(request, 'Student not found.')
        return redirect('/teacher/student_list/')
    except Exception as e:
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({'success': False, 'error': f'An error occurred: {str(e)}'})
        messages.error(request, f'An error occurred: {str(e)}')
        return redirect('/teacher/student_list/')
    
    
def teacher_task(request):
    try:
        search_query = request.GET.get('search', '')
        teacher_id = request.session.get('teacher_id')
        tasks = Task.objects.filter(teacher_id=teacher_id)
        
        if search_query:
            tasks = tasks.filter(
                Q(title__icontains=search_query)
            )
            
            

        
        paginator = Paginator(tasks, 8)
        page_number = request.GET.get('page', 1)
        page_obj = paginator.get_page(page_number)

        data = {
            'tasks': page_obj,
            'page_obj': page_obj,
            'search_query': search_query
        }

        return render(request, 'teacher/task_list.html', data)

    except Exception as e:
        return HttpResponse(f'Error: {e}') 
    
def get_students_by_section(request, section_id):
    """Get students by section for AJAX request"""
    try:
    
        section_map = {
            "1": "A",
            "2": "B", 
            "3": "C",
            "4": "D"
        }
        section_name = section_map.get(str(section_id))
        
        if not section_name:
            return JsonResponse({'success': False, 'error': 'Invalid section'})
        
        section = Section.objects.get(name=section_name)
        students = Student.objects.filter(section=section).values('student_id', 'first_name', 'last_name', 'email')
        
        return JsonResponse({
            'success': True,
            'students': list(students)
        })
    except Section.DoesNotExist:
        return JsonResponse({'success': False, 'error': 'Section not found'})
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)})

def send_task_notification_email(student, task, teacher):
    """Send email notification to student about new task"""
    try:
        subject = f'New Task Assignment: {task.title}'
        
        
        html_message = render_to_string('emails/task_notification.html', {
            'student': student,
            'task': task,
            'teacher': teacher,
            'deadline': task.deadline.strftime('%B %d, %Y at %I:%M %p') if task.deadline else 'No deadline set'
        })
        
        
        plain_message = strip_tags(html_message)
        
        
        send_mail(
            subject=subject,
            message=plain_message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[student.email],
            html_message=html_message,
            fail_silently=False,
        )
        
        return True
    except Exception as e:
        print(f"Error sending email to {student.email}: {e}")
        return False

def add_task(request):
    if request.method == 'POST':
        teacher_id = request.session.get('teacher_id')
        title = request.POST.get('title')
        description = request.POST.get('description')
        section = request.POST.get('section')
        deadline_date = request.POST.get('deadline_date')
        deadline_time = request.POST.get('deadline_time')
        selected_students = request.POST.getlist('selected_students')
        send_email_notification = request.POST.get('send_email_notification') == 'on'

        if deadline_date and deadline_time:
            deadline_str = f"{deadline_date} {deadline_time}"  # '2025-06-15 14:30'
        else:
            deadline_str = None

        deadline = None
        if deadline_str:
            deadline = datetime.strptime(deadline_str, '%Y-%m-%d %H:%M')

        data = {
            'teacher_id':teacher_id,
            'title':title,
            'description':description,
            'section':section,
            'deadline':deadline,
        }

        
        if not (teacher_id and title and description and section):
            messages.error(request, "All fields are required.")
            return redirect('add_task', data)

        try:
            teacher = Teacher.objects.get(pk=teacher_id)
            task = Task.objects.create(
                teacher=teacher,
                title=title,
                section = Section.objects.get(pk=section),
                description=description,
                deadline=deadline if deadline else None
            )
            
            
            if selected_students:
                students = Student.objects.filter(student_id__in=selected_students)
            else:
                
                students = Student.objects.filter(section=section)
            
    
            for student in students:
                AssignedTask.objects.create(
                    task = task,
                    student = student,
                    section = Section.objects.get(pk=section),
                )
                
            
                if send_email_notification:
                    send_task_notification_email(student, task, teacher)

            messages.success(request, "Task added successfully!")
            if send_email_notification:
                messages.success(request, f"Email notifications sent to {students.count()} students.")
            return redirect('/teacher/task_list/')  
        except Teacher.DoesNotExist:
            messages.error(request, "Teacher not found.")
            return redirect('add_task')

    return render(request, 'teacher/add_task.html')

def  edit_task(request, id):
    try:
        if request.method == 'POST':
            

            task = Task.objects.get(pk=id)

            title = request.POST.get('title')
            description = request.POST.get('description')
            deadline = request.POST.get('deadline')
            
            
            
            task.title = title
            task.description = description
            task.deadline = deadline
            task.save()

            messages.success(request, 'Task updated successfully!')
            return redirect('/teacher/task_list/')
        else:
            teacherObj = Task.objects.get(pk=id)
            
            data = {
                'task': teacherObj,
            }
            
            return render(request,'teacher/edit_task.html', data)
    except Exception as e:
        messages.error(request, f'An error occurred: {str(e)}')
        return redirect('/teacher/task_list')
    
def delete_task(request, id):
    try:
        if request.method == 'POST':
            task = Task.objects.get(pk=id)
            task_title = task.title
            task.delete()
            
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({
                    'success': True, 
                    'message': f'Task "{task_title}" has been deleted successfully!'
                })
            
            messages.success(request, f'Task "{task_title}" has been deleted successfully!')
            return redirect('/teacher/task_list/')
        else:
            task = Task.objects.get(pk=id)
            data = {
                'task': task
            }
            return render(request, 'teacher/delete_task.html', data)
    except Task.DoesNotExist:
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({'success': False, 'error': 'Task not found.'})
        messages.error(request, 'Task not found.')
        return redirect('/teacher/task_list/')
    except Exception as e:
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({'success': False, 'error': f'An error occurred: {str(e)}'})
        messages.error(request, f'An error occurred: {str(e)}')
        return redirect('/teacher/task_list/')
    

def assignment_grading(request):
    teacher_id = request.session.get('teacher_id')
    if not teacher_id:
    
        return redirect('login')

    
    tasks = Task.objects.filter(teacher_id=teacher_id)


    assigned_tasks = AssignedTask.objects.filter(task__in=tasks).select_related('student', 'student__section', 'task')

    
    data = []
    for assigned in assigned_tasks:
        data.append({
            'id': assigned.id, 
            'task_title': assigned.task.title,
            'student_name': f"{assigned.student}",
            'student_section': assigned.student.section.name if assigned.student.section else '',
            'status': assigned.status,
            'rating': assigned.rating,
            'assigned_date': assigned.assigned_at,
            'submission_file': assigned.submission_file.url if assigned.submission_file else '',
        })

    return render(request, "teacher/assignments_grading.html", {'assigned_tasks': data})

def teacher_profile(request):
    try:
        teacher_id = request.session.get('teacher_id')
        teacher = Teacher.objects.get(teacher_id=teacher_id)
        teacher = {
            'teacher':teacher
        }
        return render(request, "teacher/profile.html",teacher)
    except Exception as e:
            return HttpResponse(f'Error: {e}')


def edit_teacher(request, teacher_id):
    try:
        if request.method == 'POST':
            
            teacherObj = Teacher.objects.get(pk=teacher_id)

            
            username = request.POST.get('username')
            first_name = request.POST.get('first_name')
            middle_name = request.POST.get('middle_name')
            last_name = request.POST.get('last_name')
            suffix = request.POST.get('suffix')
            gender = request.POST.get('gender')
            birth_date = request.POST.get('birth_date')
            contact_number = request.POST.get('contact_number')
            email = request.POST.get('email')
            
            if Teacher.objects.filter(username=username).exclude(teacher_id=teacher_id).exists():
                messages.error(request, 'Username already exists. Please choose a different username.')
                return redirect(f'/teacher/edit_student/{teacher_id}')
            
            
            teacherObj.first_name = first_name
            teacherObj.middle_name = middle_name
            teacherObj.last_name = last_name
            teacherObj.suffix = suffix
            teacherObj.username = username
            teacherObj.gender = gender
            teacherObj.birth_date = birth_date
            teacherObj.contact_number = contact_number
            teacherObj.email = email
            teacherObj.save()

            messages.success(request, 'Student updated successfully!')
            return redirect('/teacher/profile/')
        else:
            teacherObj = Teacher.objects.get(pk=teacher_id)
            
            data = {
                'teacher': teacherObj,
            }
            
            return render(request,'teacher/edit_teacher.html', data)
    except Exception as e:
        messages.error(request, f'An error occurred: {str(e)}')
        return redirect('/teacher/profile')




@teacher_login_required
def grade_task(request, id):
    try:
        if request.method == 'POST':
            assigned_task = AssignedTask.objects.get(pk=id)
            rating = request.POST.get('rating')
            feedback = request.POST.get('feedback')

            if not rating:
                messages.error(request, 'Rating is required!')
                return redirect(f'/teacher/grade_task/{id}/')

            assigned_task.status = "graded"
            assigned_task.rating = rating
            assigned_task.feedback = feedback
            assigned_task.save()
            
            messages.success(request, 'Task graded successfully!')
            return redirect('/teacher/grading/')
        else:
            assigned_task = AssignedTask.objects.get(pk=id)
            data = {
                'assigned_task': assigned_task
            }
            return render(request, 'teacher/rating.html', data)
    except AssignedTask.DoesNotExist:
        messages.error(request, 'Task not found.')
        return redirect('/teacher/grading/')
    except Exception as e:
        messages.error(request, f'An error occurred: {str(e)}')
        return redirect('/teacher/grading/')

@teacher_login_required
def view_assigned_task(request, id):
    """View detailed information about an assigned task"""
    try:
        assigned_task = AssignedTask.objects.select_related('student', 'task', 'student__section').get(pk=id)
        
    
        teacher_id = request.session.get('teacher_id')
        if assigned_task.task.teacher_id != teacher_id:
            messages.error(request, 'You do not have permission to view this task.')
            return redirect('/teacher/grading/')
        
        context = {
            'assigned_task': assigned_task,
            'student': assigned_task.student,
            'task': assigned_task.task,
        }
        return render(request, 'teacher/view_assigned_task.html', context)
    except AssignedTask.DoesNotExist:
        messages.error(request, 'Task not found.')
        return redirect('/teacher/grading/')
    except Exception as e:
        messages.error(request, f'An error occurred: {str(e)}')
        return redirect('/teacher/grading/')

@teacher_login_required
def delete_assigned_task(request, id):
    """Delete an assigned task"""
    try:
        if request.method == 'POST':
            assigned_task = AssignedTask.objects.get(pk=id)
            
    
            teacher_id = request.session.get('teacher_id')
            if assigned_task.task.teacher_id != teacher_id:
                if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                    return JsonResponse({'success': False, 'error': 'You do not have permission to delete this task.'})
                messages.error(request, 'You do not have permission to delete this task.')
                return redirect('/teacher/grading/')
            
            task_title = assigned_task.task.title
            student_name = f"{assigned_task.student}"
            
            assigned_task.delete()
            
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({
                    'success': True, 
                    'message': f'Task "{task_title}" for {student_name} has been deleted successfully!'
                })
            
            messages.success(request, f'Task "{task_title}" for {student_name} has been deleted successfully!')
            return redirect('/teacher/grading/')
        else:
            assigned_task = AssignedTask.objects.select_related('student', 'task').get(pk=id)
            
            # 
            teacher_id = request.session.get('teacher_id')
            if assigned_task.task.teacher_id != teacher_id:
                messages.error(request, 'You do not have permission to delete this task.')
                return redirect('/teacher/grading/')
            
            context = {
                'assigned_task': assigned_task,
                'student': assigned_task.student,
                'task': assigned_task.task,
            }
            return render(request, 'teacher/delete_assigned_task.html', context)
    except AssignedTask.DoesNotExist:
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({'success': False, 'error': 'Task not found.'})
        messages.error(request, 'Task not found.')
        return redirect('/teacher/grading/')
    except Exception as e:
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({'success': False, 'error': f'An error occurred: {str(e)}'})
        messages.error(request, f'An error occurred: {str(e)}')
        return redirect('/teacher/grading/')

@teacher_login_required
def edit_grade(request, id):
    """Edit the grade of an already graded task"""
    try:
        if request.method == 'POST':
            assigned_task = AssignedTask.objects.get(pk=id)
            rating = request.POST.get('rating')
            feedback = request.POST.get('feedback')

            if not rating:
                messages.error(request, 'Rating is required!')
                return redirect(f'/teacher/edit_grade/{id}/')

            # Check if the teacher owns this task
            teacher_id = request.session.get('teacher_id')
            if assigned_task.task.teacher_id != teacher_id:
                messages.error(request, 'You do not have permission to edit this grade.')
                return redirect('/teacher/grading/')

            assigned_task.rating = rating
            assigned_task.feedback = feedback
            assigned_task.save()
            
            messages.success(request, 'Grade updated successfully!')
            return redirect('/teacher/grading/')
        else:
            assigned_task = AssignedTask.objects.get(pk=id)
            
            # Check if the teacher owns this task
            teacher_id = request.session.get('teacher_id')
            if assigned_task.task.teacher_id != teacher_id:
                messages.error(request, 'You do not have permission to edit this grade.')
                return redirect('/teacher/grading/')
            
            data = {
                'assigned_task': assigned_task
            }
            return render(request, 'teacher/edit_grade.html', data)
    except AssignedTask.DoesNotExist:
        messages.error(request, 'Task not found.')
        return redirect('/teacher/grading/')
    except Exception as e:
        messages.error(request, f'An error occurred: {str(e)}')
        return redirect('/teacher/grading/')

@teacher_login_required
def teacher_changepass(request, teacher_id):
    try:
        if request.method == 'POST':
            teacher = Teacher.objects.get(pk=teacher_id)
            current_password = request.POST.get('current_password')
            new_password = request.POST.get('new_password')
            confirm_password = request.POST.get('confirm_password')

            # First verify the current password
            if not check_password(current_password, teacher.password):
                messages.error(request, 'Current password is incorrect.')
                return redirect(f'/teacher/teacher_changepass/{teacher_id}')

            if not new_password or not confirm_password:
                messages.error(request, 'Please fill out both new password fields.')
                return redirect(f'/teacher/teacher_changepass/{teacher_id}')

            if new_password != confirm_password:
                messages.error(request, 'New password and confirm password do not match!')
                return redirect(f'/teacher/teacher_changepass/{teacher_id}')

            # Check password strength
            strength, feedback = check_password_strength(new_password)
            if strength < 3:
                messages.error(request, 'Password is too weak. Please make sure it meets all requirements: ' + ', '.join(feedback))
                return redirect(f'/teacher/teacher_changepass/{teacher_id}')

            # Update the password
            teacher.password = make_password(new_password)
            teacher.save()
            messages.success(request, 'Password changed successfully!')
            return redirect('/teacher/profile/')
        else:
            teacher = Teacher.objects.get(pk=teacher_id)
            return render(request, 'teacher/teacher_changepass.html', {'teacher': teacher})
    except Teacher.DoesNotExist:
        messages.error(request, "User not found.")
        return redirect('/teacher/profile/')
    except Exception as e:
        messages.error(request, f"Error changing password: {e}")
        return redirect('/teacher/profile/')

@teacher_login_required
def download_submission_file(request, assigned_task_id):
    """Download submission file with proper headers for all browsers"""
    try:
        assigned_task = AssignedTask.objects.select_related('task', 'student').get(pk=assigned_task_id)

        teacher_id = request.session.get('teacher_id')
        if assigned_task.task.teacher_id != teacher_id:
            messages.error(request, 'You do not have permission to download this file.')
            return redirect('/teacher/grading/')
        
        
        if not assigned_task.submission_file:
            messages.error(request, 'No file found for this submission.')
            return redirect('/teacher/grading/')
    
        file_path = assigned_task.submission_file.path
        file_name = assigned_task.submission_file.name.split('/')[-1]  
        
        
        if not os.path.exists(file_path):
            messages.error(request, 'File not found on server.')
            return redirect('/teacher/grading/')
        
        
        with open(file_path, 'rb') as file:
            file_content = file.read()
        
        
        response = HttpResponse(file_content, content_type='application/octet-stream')
        
    
        response['Content-Disposition'] = f'attachment; filename="{file_name}"'
        
        
        response['Content-Length'] = len(file_content)
        response['Cache-Control'] = 'no-cache, no-store, must-revalidate'
        response['Pragma'] = 'no-cache'
        response['Expires'] = '0'
        
        return response
        
    except AssignedTask.DoesNotExist:
        messages.error(request, 'Assignment not found.')
        return redirect('/teacher/grading/')
    except Exception as e:
        messages.error(request, f'Error downloading file: {str(e)}')
        return redirect('/teacher/grading/')

@student_login_required
def download_student_submission(request, assigned_task_id):
    """Download submission file for students (their own submissions)"""
    try:
        student_id = request.session.get('student_id')
        assigned_task = AssignedTask.objects.select_related('task', 'student').get(pk=assigned_task_id)
        
        # Check if the student owns this submission
        if assigned_task.student.student_id != student_id:
            messages.error(request, 'You do not have permission to download this file.')
            return redirect('/student/assignments-exams/')
        
        # Check if file exists
        if not assigned_task.submission_file:
            messages.error(request, 'No file found for this submission.')
            return redirect('/student/assignments-exams/')
        
        # Get file path and name
        file_path = assigned_task.submission_file.path
        file_name = assigned_task.submission_file.name.split('/')[-1]  # Get just the filename
        
        # Check if file exists on disk
        if not os.path.exists(file_path):
            messages.error(request, 'File not found on server.')
            return redirect('/student/assignments-exams/')
        
        # Open and read the file
        with open(file_path, 'rb') as file:
            file_content = file.read()
        
        # Create response with proper headers for all browsers
        response = HttpResponse(file_content, content_type='application/octet-stream')
        
        # Set filename for download (works across all browsers)
        response['Content-Disposition'] = f'attachment; filename="{file_name}"'
        
        # Additional headers for better compatibility
        response['Content-Length'] = len(file_content)
        response['Cache-Control'] = 'no-cache, no-store, must-revalidate'
        response['Pragma'] = 'no-cache'
        response['Expires'] = '0'
        
        return response
        
    except AssignedTask.DoesNotExist:
        messages.error(request, 'Assignment not found.')
        return redirect('/student/assignments-exams/')
    except Exception as e:
        messages.error(request, f'Error downloading file: {str(e)}')
        return redirect('/student/assignments-exams/')

def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        role = request.POST.get('role')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')

        # Validate input
        if not all([username, password, confirm_password, role, first_name, last_name, email]):
            messages.error(request, 'All fields are required.')
            return redirect('register')

        if password != confirm_password:
            messages.error(request, 'Passwords do not match.')
            return redirect('register')

        # Check password strength
        strength, feedback = check_password_strength(password)
        if strength < 3:
            messages.error(request, 'Password is too weak. Please make sure it meets all requirements: ' + ', '.join(feedback))
            return redirect('register')

        try:
            if role == 'student':
                # Check if username already exists
                if Student.objects.filter(username=username).exists():
                    messages.error(request, 'Username already exists.')
                    return redirect('register')

                # Create new student
                student = Student.objects.create(
                    username=username,
                    password=make_password(password),
                    first_name=first_name,
                    last_name=last_name,
                    email=email
                )
                messages.success(request, 'Student registration successful! Please login.')
                return redirect('login')

            elif role == 'teacher':
                # Check if username already exists
                if Teacher.objects.filter(username=username).exists():
                    messages.error(request, 'Username already exists.')
                    return redirect('register')

                # Create new teacher
                teacher = Teacher.objects.create(
                    username=username,
                    password=make_password(password),
                    first_name=first_name,
                    last_name=last_name,
                    email=email
                )
                messages.success(request, 'Teacher registration successful! Please login.')
                return redirect('login')

            else:
                messages.error(request, 'Invalid role selected.')
                return redirect('register')

        except Exception as e:
            messages.error(request, f'Registration failed: {str(e)}')
            return redirect('register')

    return render(request, 'layout/Register.html')
