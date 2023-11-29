from django.urls import path
from subject.views import SubjectView

urlpatterns = [path("<int:id>", SubjectView.as_view())]
