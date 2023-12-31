from django.db import models

from subject.models import Subject
from teacher.models import Teacher


class Grade(models.Model):
    name = models.CharField(max_length=30, primary_key=True)
    description = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.name}"


class Section(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=30)
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.name}"


class SectionSubject(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)


class SectionAttendance(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
