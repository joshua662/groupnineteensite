from django.urls import path
from . import views
from django.contrib import messages

urlpatterns = [
    # General 
    path("", views.landing_page, name="landing_page"),
    path("login/", views.login_view, name="login"),
    path("register/", views.register_view, name="register"),
    path("student_logout/", views.student_logout, name="student_logout"),
    path("teacher_logout/", views.teacher_logout, name="teacher_logout"),
    path("teacher_registration/", views.teacher_registration),
    path("teacher/grade_task/<int:id>/", views.grade_task),

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
    path("teacher/edit_student_partial/<int:id>/", views.edit_student_partial, name="edit_student_partial"),
    path("teacher/get_students_by_section/<int:section_id>/", views.get_students_by_section, name="get_students_by_section"),
    path("teacher/view_assigned_task/<int:id>/", views.view_assigned_task, name="view_assigned_task"),
    path("teacher/assigned_task_detail_partial/<int:assigned_task_id>/", views.assigned_task_detail_partial, name="assigned_task_detail_partial"),
    path("teacher/edit_grade_partial/<int:assigned_task_id>/", views.edit_grade_partial, name="edit_grade_partial"),
    path("teacher/delete_assigned_task_partial/<int:assigned_task_id>/", views.delete_assigned_task_partial, name="delete_assigned_task_partial"),
    path("teacher/grade_task_partial/<int:assigned_task_id>/", views.grade_task_partial, name="grade_task_partial"),
    path("teacher/delete_assigned_task/<int:id>/", views.delete_assigned_task, name="delete_assigned_task"),
    path("teacher/edit_grade/<int:id>/", views.edit_grade, name="edit_grade"),
    path("teacher/download_submission/<int:assigned_task_id>/", views.download_submission_file, name="download_submission_file"),
    
    # Student URLs
    path("student/dashboard/", views.student_dashboard, name="student_dashboard"),
    path("student/course-material/", views.student_course_material, name="student_course_material"),
    path("student/assignments-exams/", views.student_assignments_exams, name="student_assignments_exams"),
    path("student/classroom-discussion/", views.student_classroom_discussion, name="student_classroom_discussion"),
    path("student/profile-settings/", views.student_profile_settings, name="student_profile_settings"),
    path('student/edit_student/<int:student_id>/',views.edit_student),
    path("student/task_description/<int:id>/", views.task_description, name="task_description"),
    path("student/student_changepass/<int:student_id>/", views.student_changepass),
    path("student/download_submission/<int:assigned_task_id>/", views.download_student_submission, name="download_student_submission"),
    path("student/notifications/", views.student_notifications, name="student_notifications"),
    path("student/mark_notification_read/<int:notification_id>/", views.mark_notification_read, name="mark_notification_read"),
    path("student/get_unread_notifications_count/", views.get_unread_notifications_count, name="get_unread_notifications_count"),
]

