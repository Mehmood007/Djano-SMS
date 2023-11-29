from django.urls import path
from fee.views import FeeView

urlpatterns = [path("<int:id>", FeeView.as_view())]
