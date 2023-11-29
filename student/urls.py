from django.urls import path
from student.views import StudentView

urlpatterns = [path("<int:id>", StudentView.as_view())]
