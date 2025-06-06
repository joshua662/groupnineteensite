from django.urls import path
from . import views

urlpatterns = [
    path("", views.landing_page),
    path("login", views.login_view, name="login"),
    path("home/dashboard", views.home_dashboard, name="home_dashboard"),
    path("teacher/dashboard/", views.teacher_dashboard, name="teacher_dashboard"),
    path("student/dashboard/", views.student_dashboard, name="student_dashboard"),
    path('landingpage', views.landing_page), 
    path('home/post/', views.Post),
    path('home/task/', views.Task),
    path('home/media/', views.Media),
    path('home/team/', views.Team),
    path('home/signin/', views.SignIn),
    path('logout/', views.logout),
    path('user/add/', views.add_student),
    path("register/", views.register),
]

