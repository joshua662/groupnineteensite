from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.login_view),
    path("teacher/dashboard/", views.teacher_dashboard),
    path("student/dashboard/", views.student_dashboard),
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

