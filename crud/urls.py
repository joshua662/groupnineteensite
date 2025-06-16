from django.urls import path
from . import views
from django.contrib import messages

urlpatterns = [
    # General 
    path("", views.landing_page, name="landing_page"),
    path("student_login/", views.student_login, name="student_login"),
    path("student_logout/", views.student_logout, name="student_logout"),
    path("teacher_login/", views.teacher_login, name="teacher_login"),
    path("teacher_logout/", views.teacher_logout, name="teacher_logout"),
    path("teacher_registration/", views.teacher_registration),


    # Teacher URLs
    path("teacher/dashboard/", views.teacher_dashboard, name="teacher_dashboard"),
    path("teacher/student_list/", views.teacher_student),
    path("teacher/task_list/", views.teacher_task),
    path("teacher/add_task/", views.add_task, name="add_task"),
    path("teacher/edit_task/<int:id>/", views.edit_task, name="edit_task"),
    path("teacher/delete_task/<int:id>/", views.delete_task, name="delete_task"),
    path("teacher/profile/", views.teacher_profile),
    path("teacher/edit_teacher/<int:teacher_id>/", views.edit_teacher),
    path("teacher/teacher_changepass/<int:teacher_id>/", views.teacher_changepass),
    path("teacher/grading/", views.assignment_grading),
    path("teacher/add_student/", views.add_student, name="add_student"),
    path("teacher/delete_student/<int:id>/", views.delete_student1, name="delete_student"),
    path("teacher/edit_student/<int:id>/", views.edit_student1, name="edit_student"),
    
   
    # Student URLs
    path("student/dashboard/", views.student_dashboard, name="student_dashboard"),
    path("student/course-material/", views.student_course_material, name="student_course_material"),
    path("student/assignments-exams/", views.student_assignments_exams, name="student_assignments_exams"),
    path("student/classroom-discussion/", views.student_classroom_discussion, name="student_classroom_discussion"),
    path("student/profile-settings/", views.student_profile_settings, name="student_profile_settings"),
    path('student/edit_student/<int:student_id>/',views.edit_student),
    path("student/task_description/<int:id>/", views.task_description),
    path("student/student_changepass/<int:student_id>/", views.student_changepass),
    
]

