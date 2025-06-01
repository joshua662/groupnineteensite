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
            if hasattr(user, "profile") and user.profile.role == "teacher":
                return redirect("teacher_dashboard")
            elif hasattr(user, "profile") and user.profile.role == "student":
                return redirect("student_dashboard")
            else:
                return redirect("home")  # fallback
        else:
            return render(request, "layout/Login.html", {"error": "Invalid credentials"})
    return render(request, "layout/Login.html")

def landing_page(request):
    return render(request, 'Home/LandingPage.html')

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

        try:
            gender_obj = Genders.objects.get(pk=gender_id)
            Student.objects.create(
                full_name=full_name,
                gender=gender_obj,
                birth_date=birth_date,
                address=address,
                email=email,
                contact_number=contact_number,
                username=username,
                password=password
            )
            messages.success(request, "Student added successfully!")
            return redirect('add_student')
        except Exception as e:
            messages.error(request, f"Error: {e}")
            return render(request, 'student/AddStudent.html', {'genders': genders})
    return render(request, 'student/AddStudent.html', {'genders': genders})

@login_required
def teacher_dashboard(request):
    return render(request, "teacher/dashboard.html")

@login_required
def student_dashboard(request):
    return render(request, "student/dashboard.html")

def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        role = request.POST.get("role")
        email = request.POST.get("email")
        if User.objects.filter(username=username).exists():
            return render(request, "layout/Register.html", {"error": "Username already exists"})
        user = User.objects.create_user(username=username, password=password, email=email)
        user.save()
        user.profile.role = role
        user.profile.save()
        return redirect("login")
    return render(request, "layout/Register.html")