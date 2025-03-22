from django.db import models
from django.contrib.auth.models import User

class Admin(models.Model):
    name = models.CharField(max_length=255)
    designation = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=10)
    email = models.EmailField(unique=True)
    
    def _str_(self):
        return self.name
    
class Student(models.Model):
    DEPARTMENT_CHOICES = [
        ('CSE', 'Computer Science & Engineering'),
        ('ECE', 'Electronics & Communication Engineering'),
        ('ME', 'Mechanical Engineering'),
        ('EE', 'Electrical Engineering'),
        ('CE', 'Civil Engineering'),
        ('IT', 'Information Technology'),
    ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Django User model for authentication
    reg_no = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    department = models.CharField(
        max_length=20, 
        choices=DEPARTMENT_CHOICES, 
        default='CSE'
    )
    
    admin_obj = models.ForeignKey(Admin, on_delete=models.CASCADE, related_name="students")

    def _str_(self):
        return self.name

class ExamHall(models.Model):
    hall_name = models.CharField(max_length=255)
    capacity = models.IntegerField()
    floor = models.IntegerField()
    admin_id = models.ForeignKey(Admin, on_delete=models.CASCADE, related_name="halls")
    student_obj = models.OneToOneField(Student, on_delete=models.CASCADE, null=True)

    def _str_(self):
        return self.hall_name

class Exam(models.Model):
    exam_name = models.CharField(max_length=255)
    exam_date = models.DateField()
    exam_venue = models.CharField(max_length=255)
    student_obj = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True, blank=True, related_name="exams")
    exam_hall_obj = models.ForeignKey(ExamHall, on_delete=models.CASCADE, null=True)

    def _str_(self):
        return self.exam_name

class SeatAllocation(models.Model):
    seat_no = models.CharField(max_length=10)
    allocation_date = models.DateField(auto_now_add=True)
    reg_no = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="seat_allocations")
    exam_obj = models.ForeignKey(Exam, on_delete=models.CASCADE, related_name="seat_allocations")

    def _str_(self):
        return self.seat_no