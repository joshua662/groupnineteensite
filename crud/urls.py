from django.urls import path
from . import views

urlpatterns = [
    path('landingpage', views.landing_page),  # Landing page at root
    path('login/', views.Login),
    path('home/dashboard/', views.Dashboard),
    path('home/post/', views.Post),
    path('home/pages/', views.Pages),
    path('home/media/', views.Media),
    path('home/team/', views.Team),
    path('home/signin/', views.SignIn),
    path('logout/', views.logout),
]