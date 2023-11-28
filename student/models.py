from django.db import models
from grade.models import *


class Student(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=30)
    phone = models.CharField(max_length=14)
    email = models.CharField(max_length=30)
    address = models.CharField(max_length=30)


class Result(models.Model):
    result_types = (
        (1, "First Term"),
        (2, "Second Term"),
        (3, "Final Exam")
    )
    result_type = models.IntegerField(choices=result_types, default=3)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    total_marks = models.DecimalField(max_digits=5, decimal_places=2)
    achieved_marks = models.DecimalField(max_digits=5, decimal_places=2)
    

class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    status = models.CharField(max_length=10)
    day = models.DateField(auto_now_add=True)