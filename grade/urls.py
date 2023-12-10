from django.urls import path

from .views import *

urlpatterns = [
    path("<int:id>", class_students, name="class_students"),
    path("<int:id>/<int:section_id>", section_students, name="section_students"),
    path(
        "<int:id>/<int:section_id>/attendance_form",
        section_attendance_form,
        name="section_attendance_form",
    ),
    path(
        "<int:id>/<int:section_id>/result_form",
        section_result_form,
        name="section_result_form",
    ),
]
