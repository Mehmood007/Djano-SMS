from django.urls import path

from .views import *

urlpatterns = [
    path("<int:id>", teacher_dashboard, name="teacher_dashboard"),
    path("<int:id>/subjects", teacher_subjects, name="teacher_subjects"),
    path(
        "<int:id>/attendence_classes",
        teacher_attendence_classes,
        name="teacher_attendence_classes",
    ),
]
