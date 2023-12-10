from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views import View


# /teacher/<teacher_id>
def teacher_dashboard(request: HttpRequest, id: int) -> HttpResponse:
    return render(request, "teacher_dashboard.html")


# /teacher/<teacher_id>/subjects
def teacher_subjects(request: HttpRequest, id: int) -> HttpResponse:
    return render(request, "teacher_subjects.html")


# /teacher/<teacher_id>/attendence_classes
def teacher_attendence_classes(request: HttpRequest, id: int) -> HttpResponse:
    return render(request, "teacher_attendence_classes.html")
