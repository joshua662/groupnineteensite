from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.Login),
    path('home/dashboard/', views.Dashboard, name='dashboard'),
    path('home/post/', views.Post),
    path('home/pages/', views.Pages),
    path('home/media/', views.Media),
    path('home/team/', views.Team),
    path('home/signin/', views.SignIn),
    path('home/signup/', views.SignUp),
]