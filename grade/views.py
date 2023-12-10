from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views import View


# /grade/<class_id>
def class_students(request: HttpRequest, id: int) -> HttpResponse:
    return render(request, "class_students_list.html")


# /grade/<class_id>/<section_id>
def section_students(request: HttpRequest, id: int, section_id: int) -> HttpResponse:
    return render(request, "section_students_list.html")


# /grade/<class_id>/<section_id>/attendance
def section_attendance_form(
    request: HttpRequest, id: int, section_id: int
) -> HttpResponse:
    arr = [1, 2, 3, 4, 5]
    context = {"arr": arr}
    return render(request, "students_attendance_form.html", context)


# /grade/<class_id>/<section_id>/result
def section_result_form(request: HttpRequest, id: int, section_id: int) -> HttpResponse:
    arr = [1, 2, 3, 4, 5]
    context = {"arr": arr}
    return render(request, "students_result_form.html", context)
