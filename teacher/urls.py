from django.urls import path
from teacher.views import TeacherView

urlpatterns = [path("<int:id>", TeacherView.as_view())]
