from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Genders, Profile

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)

            user_role = user.profile.role if hasattr(user, 'profile') else 'unknown'

            if user.is_superuser or user_role == "admin":
                messages.success(request, f"Welcome, Admin {user.username}!")
                return redirect("home_dashboard")
            elif user_role == "teacher":
                messages.success(request, f"Welcome, Teacher {user.username}!")
                return redirect("teacher_dashboard")
            elif user_role == "student":
                messages.success(request, f"Welcome, Student {user.username}!")
                return redirect("student_dashboard")
            else:
                messages.success(request, f"Welcome, {user.username}!")
                return redirect("layout/Login.html")
        else:
            messages.error(request, "Invalid credentials")
            return render(request, "layout/Login.html")
    return render(request, "layout/Login.html")



@login_required
def teacher_dashboard(request):
    if not hasattr(request.user, 'profile') or request.user.profile.role != 'teacher':
        messages.warning(request, "You do not have permission to access this page.")
        return redirect('login') 
    return render(request, "teacher/dashboard.html")

@login_required
def student_dashboard(request):
    if not hasattr(request.user, 'profile') or request.user.profile.role != 'student':
        messages.warning(request, "You do not have permission to access this page.")
        return redirect('login') 
    return render(request, "student/dashboard.html")

@login_required
def home_dashboard(request):
    if not request.user.is_superuser and (not hasattr(request.user, 'profile') or request.user.profile.role != 'admin'):
        messages.warning(request, "You do not have permission to access this page.")
        return redirect('login')
    return render(request, "Home/Dashboard.html")

def landing_page(request):
    return render(request, 'layout/LandingPage.html')

def Dashboard(request):
    return render(request, 'Home/Dashboard.html')

def Post(request):
    return render(request, 'Home/Post.html')

def Task(request):
    return render(request, 'Home/Task.html')

def Media(request):
    return render(request, 'Home/Media.html')

def Team(request):
    return render(request, 'Home/Team.html')

def SignIn(request):
    return render(request, 'Home/SignIn.html')

def logout(request):
    auth_logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('/login/')

def add_student(request):
    genders = Genders.objects.all()
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        gender_id = request.POST.get('gender')
        birth_date = request.POST.get('birth_date')
        address = request.POST.get('address')
        email = request.POST.get('email')
        contact_number = request.POST.get('contact_number')
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return render(request, 'student/AddStudent.html', {'genders': genders})

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists. Please choose a different one.")
            return render(request, 'student/AddStudent.html', {'genders': genders})

        try:
            user = User.objects.create_user(username=username, password=password, email=email)

    
            profile = user.profile 

            profile.role = 'student'

            gender_obj = None
            if gender_id:
                try:
                    gender_obj = Genders.objects.get(pk=gender_id)
                except Genders.DoesNotExist:
                    messages.warning(request, "Selected gender not found for student.")

            profile.full_name = full_name
            profile.gender = gender_obj
            profile.birth_date = birth_date
            profile.address = address
            profile.contact_number = contact_number
            profile.save() 

            messages.success(request, f"Student '{username}' added successfully!")
            return redirect('add_student')
        except Exception as e:
            messages.error(request, f"Error adding student: {e}")
            return render(request, 'student/AddStudent.html', {'genders': genders})
    return render(request, 'student/AddStudent.html', {'genders': genders})



def register(request):
    genders = Genders.objects.all()
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")
        role = request.POST.get("role") 
        email = request.POST.get("email")
        full_name = request.POST.get("full_name")
        birth_date = request.POST.get("birth_date")
        address = request.POST.get("address")
        contact_number = request.POST.get("contact_number")
        gender_id = request.POST.get("gender") 

        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return render(request, "layout/Register.html", {'genders':genders, 'username': username, 'email': email, 'role': role, 'full_name': full_name, 'birth_date': birth_date, 'address': address, 'contact_number': contact_number, 'gender_id': gender_id})

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists. Please choose a different one.")
            return render(request, "layout/Register.html", {'genders':genders, 'username': username, 'email': email, 'role': role, 'full_name': full_name, 'birth_date': birth_date, 'address': address, 'contact_number': contact_number, 'gender_id': gender_id})

        try:
           
            user = User.objects.create_user(username=username, password=password, email=email)

            
            profile = user.profile
            profile.role = role

            gender_obj = None
            if gender_id:
                try:
                    gender_obj = Genders.objects.get(pk=gender_id)
                except Genders.DoesNotExist:
                    messages.warning(request, "Selected gender not found during registration.")

            profile.full_name = full_name
            profile.birth_date = birth_date
            profile.address = address
            profile.contact_number = contact_number
            profile.gender = gender_obj
            profile.save()

            if role == "student":
                login(request, user)
                messages.success(request, "Registration successful! You are now logged in.")
                return redirect("student_dashboard")
            elif role == "teacher":
                login(request, user)
                messages.success(request, "Registration successful! You are now logged in.")
                return redirect("teacher_dashboard")
            else:
                messages.success(request, "Registration successful! Please log in.")
                return redirect("login")
        except Exception as e:
            messages.error(request, f"Registration failed: {e}")
            return render(request, "layout/Register.html", {'genders':genders, 'username': username, 'email': email, 'role': role, 'full_name': full_name, 'birth_date': birth_date, 'address': address, 'contact_number': contact_number, 'gender_id': gender_id})
    return render(request, "layout/Register.html", {'genders': genders})

def student_course_material(request):
    return render(request, "student/course_material.html")

def student_assignments_exams(request):
    return render(request, "student/assignments_exams.html")

def student_classroom_discussion(request):
    return render(request, "student/classroom_discussion.html")

def student_profile_settings(request):
    return render(request, "student/profile_settings.html")

def teacher_lesson_plan_course_materials(request):
    return render(request, "teacher/lesson_plan_course_materials.html")

def teacher_assignments_grading(request):
    return render(request, "teacher/assignments_grading.html")

def teacher_student_management(request):
    return render(request, "teacher/student_management.html")

def teacher_classroom_discussions(request):
    return render(request, "teacher/classroom_discussions.html") 