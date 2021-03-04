from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    user_type_data=((1,"Admin"),(2,"Lecturer"),(3,"Student"))
    user_type=models.CharField(default=1,choices=user_type_data,max_length=10)

class Admin(models.Model):
    admin = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    objects = models.Manager()

class Lecturer(models.Model):
    lecturer = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    objects = models.Manager()

class Courses(models.Model):
    id=models.AutoField(primary_key=True)
    course_name=models.CharField(max_length=100)
    objects=models.Manager()

class Student(models.Model):
    Student = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    gender = models.CharField(max_length=10)
    address = models.TextField()
    profile_pic = models.FileField()
    birth_date = models.DateField()
    course_id = models
    objects = models.Manager()

class FeedBackStudent(models.Model):
    id = models.AutoField(primary_key=True)
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    feedback = models.TextField()
    feedback_reply = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

class FeedBackLecturer(models.Model):
    id = models.AutoField(primary_key=True)
    staff_id = models.ForeignKey(Lecturer, on_delete=models.CASCADE)
    feedback = models.TextField()
    feedback_reply=models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()






