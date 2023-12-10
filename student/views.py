from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views import View


# /student/<student_id>
def student_dashboard(request: HttpRequest, id: int) -> HttpResponse:
    return render(request, "student_dashboard.html")


# /student/<student_id>/fee_details
def student_fee_details(request: HttpRequest, id: int) -> HttpResponse:
    return render(request, "student_fee_details.html")
