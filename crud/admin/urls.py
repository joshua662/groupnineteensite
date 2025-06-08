from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='admin_dashboard'),
    path('class-teacher-management/', views.class_teacher_management, name='class_teacher_management'),
    path('user-account/', views.user_account, name='user_account'),
    path('resources-course-materials/', views.resources_course_materials, name='resources_course_materials'),
    path('system-setting-reports/', views.system_setting_reports, name='system_setting_reports'),
    path('logout/', views.logout_view, name='admin_logout'),
] 