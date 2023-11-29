from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.views import View


class FeeView(View):
    """
    All request regarding student model are handled in this class
    Function names are based on method names
    """

    # Below function is triggered upon get request
    def get(self, request: HttpRequest, id: int) -> HttpResponse:
        print(type(request))
        return HttpResponse(f"Hello Fee with id {id}")
