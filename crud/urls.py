from django.urls import path
from . import views
from django.contrib import messages

urlpatterns = [
    # General 
    path("", views.landing_page, name="landing_page"),
    path("login/", views.login_view, name="login"),
    path("register/", views.register, name="register"),
    path("logout/", views.logout_admin, name="logout"),

    # Admin URLs
    path('admin/dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('admin/class-teacher-management/', views.class_teacher_management, name='class_teacher_management'),
    path('admin/user-account/', views.user_account, name='user_account'),
    path('admin/resources-course-materials/', views.resources_course_materials, name='resources_course_materials'),
    path('admin/system-setting-reports/', views.system_setting_reports, name='system_setting_reports'),

    # Teacher URLs
    path("teacher/dashboard/", views.teacher_dashboard, name="teacher_dashboard"),
    path("teacher/lesson-plan-course-materials/", views.teacher_lesson_plan_course_materials, name="teacher_lesson_plan_course_materials"),
    path("teacher/assignments-grading/", views.teacher_assignments_grading, name="teacher_assignments_grading"),
    path("teacher/student-management/", views.teacher_student_management, name="teacher_student_management"),
    path("teacher/classroom-discussions/", views.teacher_classroom_discussions, name="teacher_classroom_discussions"),
   
    # Student URLs
    path("student/dashboard/", views.student_dashboard, name="student_dashboard"),
    path("student/course-material/", views.student_course_material, name="student_course_material"),
    path("student/assignments-exams/", views.student_assignments_exams, name="student_assignments_exams"),
    path("student/classroom-discussion/", views.student_classroom_discussion, name="student_classroom_discussion"),
    path("student/profile-settings/", views.student_profile_settings, name="student_profile_settings"),
]

