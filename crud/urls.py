from django.urls import path
from . import views

urlpatterns = [
    path("", views.landing_page),
    path("login/", views.login_view, name="login"),
    path("home/dashboard", views.home_dashboard, name="home_dashboard"),
    path("teacher/dashboard/", views.teacher_dashboard, name="teacher_dashboard"),
    path("teacher/lesson-plan-course-materials/", views.teacher_lesson_plan_course_materials, name="teacher_lesson_plan_course_materials"),
    path("teacher/assignments-grading/", views.teacher_assignments_grading, name="teacher_assignments_grading"),
    path("teacher/student-management/", views.teacher_student_management, name="teacher_student_management"),
    path("teacher/classroom-discussions/", views.teacher_classroom_discussions, name="teacher_classroom_discussions"),
    path("student/dashboard/", views.student_dashboard, name="student_dashboard"),
    path("student/course-material/", views.student_course_material, name="student_course_material"),
    path("student/assignments-exams/", views.student_assignments_exams, name="student_assignments_exams"),
    path("student/classroom-discussion/", views.student_classroom_discussion, name="student_classroom_discussion"),
    path("student/profile-settings/", views.student_profile_settings, name="student_profile_settings"),
    path('landingpage', views.landing_page), 
    path('home/post/', views.Post),
    path('home/task/', views.Task),
    path('home/media/', views.Media),
    path('home/team/', views.Team),
    path('home/signin/', views.SignIn),
    path('logout/', views.logout),
    path('user/add/', views.add_student),
    path("register/", views.register, name="register"),
]

