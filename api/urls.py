from django.urls import path
from .views import LatLongAPIView

urlpatterns = [
    path('', LatLongAPIView.as_view()),
]
