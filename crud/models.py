from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Genders(models.Model):
    class Meta:
        db_table = 'tbl_genders'

    gender_id = models.BigAutoField(primary_key=True, blank=False) 
    gender = models.CharField(max_length=56, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class Users(models.Model):
    class Meta:
        db_table = 'tbl_users'
    
    user_id = models.BigAutoField(primary_key=True, blank=False)
    full_name = models.CharField(max_length=55, blank=False)
    gender = models.ForeignKey(Genders, on_delete=models.CASCADE)
    birth_date = models.DateField(blank=False)  
    address = models.CharField(max_length=55, blank=False)  
    contact_number = models.CharField(max_length=55, blank=False)
    email = models.EmailField(max_length=55, blank=True)
    username = models.CharField(max_length=55, blank=False, unique=True)
    password = models.CharField(max_length=255, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Profile(models.Model):
    ROLE_CHOICES = (
        ('student', 'Student'),
        ('teacher', 'Teacher'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

    def __str__(self):
        return f"{self.user.username} - {self.role}"

