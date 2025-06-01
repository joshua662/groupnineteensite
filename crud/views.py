from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout as auth_logout
from django.contrib import messages
from .models import Genders  # or Genders if that's your model name

def Login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'layout/Login.html')

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
            from django.contrib import messages
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
                password=password  # In production, hash the password!
            )
            messages.success(request, "Student added successfully!")
            return redirect('add_student')
        except Exception as e:
            messages.error(request, f"Error: {e}")
            return render(request, 'student/AddStudent.html', {'genders': genders})
    return render(request, 'student/AddStudent.html', {'genders': genders})