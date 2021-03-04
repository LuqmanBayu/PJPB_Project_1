from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver

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

@receiver(post_save,sender=CustomUser)
def create_user_profile(sender,instance,created,**kwargs):
    if created:
        if instance.user_type==1:
            Admin.objects.create(admin=instance)
        if instance.user_type==2:
            Lecturer.objects.create(admin=instance,address="")
        if instance.user_type==3:
            Student.objects.create(admin=instance,course_id=Courses.objects.get(id=1),
                                    address="",profile_pic="",gender="")

@receiver(post_save,sender=CustomUser)
def save_user_profile(sender,instance,**kwargs):
    if instance.user_type==1:
        instance.admin.save()
    if instance.user_type==2:
        instance.lecturer.save()
    if instance.user_type==3:
        instance.student.save()







