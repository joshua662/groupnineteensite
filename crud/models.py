# crud/models.py

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from datetime import date
# from .models import Profile # Your Profile model


class Section(models.Model):
    name = models.CharField(max_length=1, null=True, blank=True)  

    def __str__(self):
        return f"Section {self.name}"
    

class Teacher(models.Model):
    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('others', 'Others'),
    )

    teacher_id = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100)
    suffix = models.CharField(max_length=20, null=True, blank=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    birth_date = models.DateField()
    age = models.PositiveIntegerField()
    address = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(unique=True)
    contact_number = models.CharField(max_length=20, null=True, blank=True)
    subject = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def calculate_current_age(self):
        """Calculate current age based on birth_date"""
        today = date.today()
        return today.year - self.birth_date.year - ((today.month, today.day) < (self.birth_date.month, self.birth_date.day))

    class Meta:
        db_table = 'tbl_teacher'

    def __str__(self):
         return f"{self.last_name}, {self.first_name} {self.middle_name} {self.suffix}"

class Student(models.Model):
    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    )

    student_id = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100)
    suffix = models.CharField(max_length=20, null=True, blank=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    birth_date = models.DateField()
    age = models.PositiveIntegerField()
    address = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(unique=True)
    contact_number = models.CharField(max_length=20, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    section = models.ForeignKey(Section, on_delete=models.SET_NULL, null=True, blank=True)

    def calculate_current_age(self):
        """Calculate current age based on birth_date"""
        today = date.today()
        return today.year - self.birth_date.year - ((today.month, today.day) < (self.birth_date.month, self.birth_date.day))

    class Meta:
        db_table = 'tbl_student'

    def __str__(self):
        if self.middle_name:
            middle_initial = f"{self.middle_name[0]}."
        else:
            middle_initial = ""
        return f"{self.last_name}, {self.first_name} {middle_initial} {self.suffix}"
    

class Task(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    deadline = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    section = models.ForeignKey(Section, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        db_table = 'tbl_task'

    def __str__(self):
        return self.title

class AssignedTask(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    assigned_at = models.DateTimeField(auto_now_add=True)
    submitted_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=20,
        choices=[('pending', 'Pending'), ('submitted', 'Submitted'), ('graded', 'Graded')],
        default='pending'
    )
    submission_file = models.FileField(upload_to='submissions/', null=True, blank=True) 
    section = models.ForeignKey(Section, on_delete=models.CASCADE, null=True, blank=True)
    rating = models.PositiveIntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    class Meta:
        db_table = 'tbl_assigned_task'

    def __str__(self):
        return f"{self.task.title} - {self.student.first_name} {self.student.last_name}"
    

