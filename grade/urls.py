from django.urls import path
from grade.views import GradeView

urlpatterns = [path("<int:id>", GradeView.as_view())]
