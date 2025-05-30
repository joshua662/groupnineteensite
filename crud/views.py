from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

def Login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')  # This must match the name in urls.py
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'layout/Login.html')

def Dashboard(request):
    return render(request, 'Home/Dashboard.html')

def Post(request):
    return render(request, 'Home/Post.html')

def Pages(request):
    return render(request, 'Home/Pages.html')

def Media(request):
    return render(request, 'Home/Media.html')

def Team(request):
    return render(request, 'Home/Team.html')

def SignIn(request):
    return render(request, 'Home/SignIn.html')

def SignUp(request):
    return render(request, 'Home/SignUp.html')