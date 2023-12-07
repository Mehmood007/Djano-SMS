from django.urls import path

from .views import *

urlpatterns = [
    path("<int:id>", student_dashboard, name="student_dashboard"),
    path("<int:id>/fee_details", student_fee_details, name="student_fee_details"),
]
