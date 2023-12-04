from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views import View


class StudentView(View):
    """
    All request regarding student model are handled in this class
    Function names are based on method names
    """

    # Below function is triggered upon get request
    def get(self, request: HttpRequest, id: int) -> HttpResponse:
        print(type(request))
        return render(request, "student_dashboard.html")
